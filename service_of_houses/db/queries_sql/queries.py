all_houses_valids = """ 
select  name as status, address, city  , price , description, year
from 
  (
    select 
      * 
    from 
      (
        SELECT 
          p.id, 
          status_data.name, 
          CASE WHEN length(
            trim(p.address)
          )> 0 then p.address else null end as address, 
          CASE WHEN length(
            trim(p.city)
          )> 0 then p.city else null end as city, 
          case when p.price > 0 then p.price else null end as price, 
          case when length(
            trim(p.description)
          )> 0 then p.description else null end as description, 
          case when (p.`year` is not null) then p.`year` else null end as year
        FROM 
          property p, 
          (
            select 
              property_id as property_id, 
              s.name as name 
            from 
              (
                SELECT 
                  n.* 
                FROM 
                  status_history n 
                  INNER JOIN (
                    SELECT 
                      property_id, 
                      MAX(update_date) AS update_date 
                    FROM 
                      status_history 
                    GROUP BY 
                      property_id
                  ) AS max USING (property_id, update_date)
              ) as results_status, 
              status s 
            where 
              results_status.status_id in (3, 4, 5) 
              and s.id = results_status.status_id
          ) as status_data 
        where 
          p.id = status_data.property_id
      ) as results_clean 
    WHERE 
      CONCAT(
        results_clean.address, results_clean.city, 
        results_clean.price, results_clean.description, 
        results_clean.`year`
      ) is not null
  ) as final_results 
  group by id
"""
import pandas as pd
import sys
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from sqlalchemy import exc
from db.session import get_db 
from db.queries_sql.queries import (all_houses_valids)
from db.error_messages.messages import ERROR_DATABASE_QUERIE_ALL_HOUSES, ERROR_FILTERS_NULL
from .schemas import UserRequestModel



sys.path.append('..')
from functions.functions_data import check_size_filter,iter_col_dataframe



router = APIRouter(
    prefix='/api/v1',
    tags=["propiedades"]
)





@router.post("/filter_data_houses")
async def filter_data_houses(user_request: UserRequestModel,response:Response,db: Session = Depends(get_db)):
    validation_filters = check_size_filter(user_request)
    try:
        if validation_filters:
            years = user_request.years
            cities=  user_request.cities
            status =user_request.status

            try:
                if len(years) > 0:
                    years = [int(year) for year in years]
            except ValueError:
                response.status_code = 400
                return {"message": "Has ingresado un año invalido verificar nuevamente"}

            df = pd.read_sql(all_houses_valids, db.bind)
            
            if len(user_request.years) ==0:
                years = list(set( iter_col_dataframe(df["year"])))
            if len(user_request.cities) == 0:
                cities = list(set( iter_col_dataframe( df["city"])))
            if len(user_request.status) == 0:
                status = list(set(iter_col_dataframe( df["status"])))
           
            filter_df = df[(df['city'].isin(cities)) &  df['status'].isin(status)  & df['year'].isin(years)]
            response_filter = filter_df.to_dict("records")
            response.status_code = 200

        else:
            response.status_code = 400
            response_filter =  ERROR_FILTERS_NULL
    except exc.InterfaceError:
        response.status_code = 500
        response_filter = ERROR_DATABASE_QUERIE_ALL_HOUSES
    except Exception as e:
        response.status_code = 500
        response_filter = ERROR_DATABASE_QUERIE_ALL_HOUSES
    db.close()
    return response_filter
    



@router.get("/all_houses")
async def all_properties(response:Response,db: Session = Depends(get_db)):
    try:
        data = db.execute(all_houses_valids)
        house_results = data.fetchall()
        response.status_code =200
    except exc.InterfaceError:
        house_results = ERROR_DATABASE_QUERIE_ALL_HOUSES
        response.status_code =500
    except Exception:
        house_results = ERROR_DATABASE_QUERIE_ALL_HOUSES
        response.status_code =500
    db.close()
    return house_results
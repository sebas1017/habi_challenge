def iter_col_dataframe(column):
    result = []
    for k, v in column.iteritems():
        result.append(v)
    return result

def check_size_filter(filters):
    size_filters = 0
    try:
        for filter in filters:
            if len(filter[1]) and len("".join(filter[1]).strip()) > 0:
                size_filters+=1
        if size_filters == 0:
            return False
        elif size_filters > 0:
            return True
    except   Exception as e:
        return False

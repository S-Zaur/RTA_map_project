from psycopg2 import sql


def from_rta_mc_mv(columns, values):
    select = '''SELECT region, count(*) FROM public."RTA" WHERE'''
    for i in range(len(columns)):
        select += "("

        # Фильтр для данных date
        if columns[i] == "rta_date":
            select += " {} BETWEEN '{}' and '{}'---".format(columns[i], values[i][0], values[i][1])

        # Фильтр для данных text[]
        elif columns[i] in ["weather", "nearby", "road_conditions", "participant_categories"]:
            for j in values[i]:
                if type(j) != str:
                    for k in j:
                        select += " '{}' = ANY({}) and".format(k, columns[i])
                else:
                    select += " '{}' = ANY({}) or".format(j, columns[i])

        # Фильтр для данных int и text
        else:
            for j in values[i]:
                select += " {} = '{}' or".format(columns[i], j)

        select = select[:-3] + ") and"
    select = select[:-3] + "GROUP BY region"
    return select


def from_rta_oc_mv(column, values):
    query = sql.SQL("SELECT region, count(*) FROM public.\"RTA\" where {column} = ANY(%s) group by region") \
            .format(column=sql.Identifier(column))
    return query


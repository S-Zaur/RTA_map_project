from psycopg2 import sql


def select_rta(columns, values):
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
    select = select.replace('WHGROUP','GROUP')
    return select


def select_participants(columns, values):
    select = '''SELECT region, count(*) FROM public."participants" inner join "RTA" R on R.id = participants.rta_id WHERE'''
    for i in range(len(columns)):
        select += "("

        # Фильтр для данных text[]
        if columns[i] == "violations":
            for j in values[i]:
                if j == "{}":
                    select += " {} = '{}' or".format(columns[i], j)
                else:
                    select += " '{}' = ANY({}) or".format(j, columns[i])

            # Фильтр для данных int, bool и text и years_of_driving_experience
        else:
            for j in values[i]:
                if j != "null":
                    select += " {} = '{}' or".format(columns[i], j)
                else:
                    select += " {} is NULL or".format(columns[i])
        select = select[:-3] + ") and"

    select = select[:-3] + "GROUP BY region"
    select = select.replace('WHGROUP','GROUP')
    return select


def select_vehicles(columns, values):
    select = '''SELECT region, count(*) FROM public."vehicles" join "RTA" R on R.id = vehicles.rta_id WHERE'''
    for i in range(len(columns)):
        select += "("

        for j in values[i]:
            if j != "null":
                select += " vehicles.{} = '{}' or".format(columns[i], j)
            else:
                select += " vehicles.{} is NULL or".format(columns[i])
        select = select[:-3] + ") and"

    select = select[:-3] + "GROUP BY region"
    select = select.replace('WHGROUP','GROUP')
    return select

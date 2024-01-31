def select_rta(columns, values):
    select = """SELECT region, count(*) FROM public."rta" WHERE"""
    for i in range(len(columns)):
        select += "("

        # Фильтр для данных date
        if columns[i] == "rta_date":
            select += " {} BETWEEN '{}' and '{}'---".format(
                columns[i], values[i][0], values[i][1]
            )

        # Фильтр для данных text[]
        elif columns[i] in [
            "weather",
            "nearby",
            "road_conditions",
            "participant_categories",
        ]:
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
    select = select.replace("WHGROUP", "GROUP")
    return select


def select_participants(columns, values):
    select = """SELECT region, count(*) FROM public."participants" inner join "rta" R on R.id = participants.rta_id WHERE"""
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
    select = select.replace("WHGROUP", "GROUP")
    return select


def select_vehicles(columns, values):
    select = """SELECT region, count(*) FROM public."vehicles" join "rta" R on R.id = vehicles.rta_id WHERE"""
    for i in range(len(columns)):
        select += "("

        for j in values[i]:
            if j != "null":
                select += " vehicles.{} = '{}' or".format(columns[i], j)
            else:
                select += " vehicles.{} is NULL or".format(columns[i])
        select = select[:-3] + ") and"

    select = select[:-3] + "GROUP BY region"
    select = select.replace("WHGROUP", "GROUP")
    return select


def super_select(rta_cv=None, vehicle_cv=None, participant_cv=None):
    if rta_cv is None and vehicle_cv is None and participant_cv is None:
        return """SELECT region, count(*) FROM public."rta" GROUP BY region"""
    query = """SELECT region, count(*) FROM"""
    if participant_cv is not None and vehicle_cv is not None:
        query += """"participants" JOIN "vehicles" ON participants.vehicle_id = vehicles.id 
        JOIN "rta" ON "rta".id  = vehicles.rta_id """
    elif participant_cv is not None:
        query += """ "participants" JOIN "rta" ON participants.rta_id = "rta".id"""
    elif vehicle_cv is not None:
        query += """ "vehicles" JOIN "rta" ON vehicles.rta_id = "rta".id"""
    else:
        query += """ "rta\""""
    query += """ WHERE\n"""

    if participant_cv is not None:
        for i in range(len(participant_cv[0])):
            query += "("
            if participant_cv[0][i] == "violations":
                for j in participant_cv[1][i]:
                    if j == "{}":
                        query += " {} = '{}' or".format(participant_cv[0][i], j)
                    else:
                        query += " '{}' = ANY({}) or".format(j, participant_cv[0][i])
            elif participant_cv[0][i] == "gender":
                for j in participant_cv[1][i]:
                    query += " {} = '{}' or".format(
                        participant_cv[0][i], j != "Мужчина"
                    )
            else:
                for j in participant_cv[1][i]:
                    if j != "null":
                        query += " {} = '{}' or".format(participant_cv[0][i], j)
                    else:
                        query += " {} is NULL or".format(participant_cv[0][i])
            query = query[:-3] + ") and\n"

    if vehicle_cv is not None:
        for i in range(len(vehicle_cv[0])):
            query += "("

            for j in vehicle_cv[1][i]:
                if j != "null":
                    query += " vehicles.{} = '{}' or".format(vehicle_cv[0][i], j)
                else:
                    query += " vehicles.{} is NULL or".format(vehicle_cv[0][i])
            query = query[:-3] + ") and\n"

    if rta_cv is not None:
        for i in range(len(rta_cv[0])):
            query += "("

            if rta_cv[0][i] == "rta_date":
                query += " {} BETWEEN '{}' and '{}'---".format(
                    rta_cv[0][i], rta_cv[1][i][0], rta_cv[1][i][1]
                )

            elif rta_cv[0][i] in [
                "weather",
                "nearby",
                "road_conditions",
                "participant_categories",
            ]:
                for j in rta_cv[1][i]:
                    if type(j) != str:
                        for k in j:
                            query += " '{}' = ANY({}) or".format(k, rta_cv[0][i])
                    else:
                        query += " '{}' = ANY({}) or".format(j, rta_cv[0][i])
            else:
                if len(rta_cv[1][i]) > 1:
                    query += "{} IN {}   ".format(rta_cv[0][i], tuple(rta_cv[1][i]))
                else:
                    query += "{} = '{}'   ".format(rta_cv[0][i], rta_cv[1][i][0])

            query = query[:-3] + ") and\n"

    query = query[:-4] + "\nGROUP BY region"
    return query

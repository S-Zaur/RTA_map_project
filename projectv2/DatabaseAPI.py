import os

import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from multipledispatch import dispatch
from .consts import regions
import math
from .query_generator import *

load_dotenv()


def _to_dict(res):
    result = {}
    for i in res:
        result[i[0]] = i[1]
    return result


class DatabaseApi:
    def __init__(self):
        self.connection = psycopg2.connect(os.getenv('CONN_STR'))
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()
        self.all = self.select_count_rta_by_region()

    def __del__(self):
        self.connection.close()

    def select_rta_count(self):
        query = '''select count(*) from public."RTA"'''
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def select_vehicles_count(self):
        query = '''select count(*) from public."vehicles"'''
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def select_participants_count(self):
        query = '''select count(*) from public."participants"'''
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def select_count_rta_by_region(self):
        query = '''select region, count(*) from public."RTA" group by region'''
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        return _to_dict(res)


    def select_count_rta_by_keys_values(self, keys, values):
        query = sql.SQL(select_rta(keys, values))
        self.cursor.execute(query, values)

        res = self.cursor.fetchall()
        return _to_dict(res)

    def select_count_vehicles(self, keys, values):
        query = sql.SQL(select_vehicles(keys, values))
        self.cursor.execute(query, values)

        res = self.cursor.fetchall()
        return _to_dict(res)

    def select_count_participants(self, keys, values):
        query = sql.SQL(select_participants(keys, values))
        self.cursor.execute(query, values)

        res = self.cursor.fetchall()
        return _to_dict(res)

    def rta_between(self, from_date, to_date):
        query = sql.SQL(
            "SELECT region, count(*) FROM public.\"RTA\" where \"rta_date\" BETWEEN %s and %s group by region")
        return _to_dict(self.cursor.execute(query, (from_date, to_date)))

    def as_percentage(self, res):
        for key, _ in res.items():
            res[key] /= float(self.all[key])
            res[key] *= 10000
            res[key] = math.floor(res[key])
            res[key] /= 100
        return res

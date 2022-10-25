import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from multipledispatch import dispatch
from .consts import regions
import math


class DatabaseApi:
    def __init__(self):
        self.connection = psycopg2.connect(user="postgres",
                                           password="11111",
                                           host="127.0.0.1",
                                           port="5432",
                                           database="rta")
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
        res = {}
        self.cursor.execute(query)
        for i in self.cursor.fetchall():
            if i[0] == 'Республика Крым' or i[0] == 'Севастополь':
                continue
            res[regions[i[0]]] = i[1]
        return res

    def select_count_rta_by_key_value(self, key, value):
        return self.select_count_rta_by_key_values(key, [value])

    def select_count_rta_by_key_values(self, key, values):

        query = sql.SQL("SELECT region, count(*) FROM public.\"RTA\" where {column} = ANY(%s) group by region") \
            .format(column=sql.Identifier(key))
        res = {}
        self.cursor.execute(query, (values,))
        for i in self.cursor.fetchall():
            if i[0] == 'Республика Крым' or i[0] == 'Севастополь':
                continue
            res[regions[i[0]]] = i[1]
        return res

    def rta_between(self, from_date, to_date):
        query = sql.SQL(
            "SELECT region, count(*) FROM public.\"RTA\" where \"rta_date\" BETWEEN %s and %s group by region")
        res = {}
        self.cursor.execute(query, (from_date, to_date))
        for i in self.cursor.fetchall():
            if i[0] == 'Республика Крым' or i[0] == 'Севастополь':
                continue
            res[regions[i[0]]] = i[1]
        return res

    def as_percentage(self, res):
        for key, _ in res.items():
            res[key] /= float(self.all[key])
            res[key] *= 10000
            res[key] = math.floor(res[key])
            res[key] /= 100
        return res

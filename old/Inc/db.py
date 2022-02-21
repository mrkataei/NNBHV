""""
Mr.Kataei 8/4/2021
update 2/22/2022
"""
from old import connect, config, mysqlError

# DB_HOST = config('DB_HOST')
# DB_NAME = config('DB_NAME')
# DB_USERNAME = config('DB_USERNAME')
# DB_PASSWORD = config('DB_PASSWORD')

DB_HOST = "localhost"
DB_NAME = "yourDbName"
DB_USERNAME = "root"
DB_PASSWORD = ""


def con_db():
    try:
        database = connect(
            host=DB_HOST,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return database
    except mysqlError as err:
        return "Something went wrong: {}".format(err)

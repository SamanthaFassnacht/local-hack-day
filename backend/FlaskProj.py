from typing import List, Tuple

import pyodbc
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


server = "tcp:spacetourssim.database.windows.net"
username = "USER@spacetourssim"
password = "UTSChack2018"
driver = "{ODBC Driver 13 for SQL Server}"
database = "SPACE_TOURS_SIM_MAIN"

connection = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)
cur = connection.cursor()

print("Connection established")


def getAllPlanetsInit() -> List[Tuple[str]]:
    cur.execute("SELECT * FROM Planets")
    result = cur.fetchall()

    return result


def getAllRocketNames() -> List[Tuple[str]]:
    cur.execute("SELECT MoTName from ModeofTransportation")
    results = cur.fetchall()

    return [name[0] for name in results]


def getRocketInfoFromName(name: str) -> Tuple[str]:
    cur.execute("SELECT * FROM ModeofTransportation WHERE MoTName = '" + (name) + "'")
    result = cur.fetchone()

    return result


#
# if __name__ == "__main__":
#     print(getAllPlanetsInit())
#     print(getAllRocketNames())
#     print(getRocketInfoFromName("Rocket"))

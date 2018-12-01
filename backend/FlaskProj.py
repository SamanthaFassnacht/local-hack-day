import mysql.connector
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class DatabaseConnection:
    mydb = mysql.connector.connector.connect(
        host="http://spacestourssim.database.windows.net",
        user="USER",
        passwd="UTSChack2018",
        database="SPACE_TOURS_SIM_MAIN"
    )

    def getAllPlanetsInit(self):
        cur = mydb.cursor()
        cur.execute("SELECT * FROM Planets")
        result = cur.fetchall()

        return result

    def getAllRocketNames(self):
        cur = mydb.cursor()
        cur.execute("SELECT MoTName from ModeofTransportation")
        result = cur.fetchall()

        return result

    def getRocketInfoFromName(self, name):
        cur = mydb.cursor()
        cur.execute("SELECT * FROM ModeofTransportation WHERE MoTName = %s", (name))
        result = cur.fetchone()


class PlanetsInit:
    def __init__(self):
        pass

class GetTrajectorySet:
    def __init__(self):
        pass
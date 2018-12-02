from typing import List, Tuple
import numpy as np

import pyodbc
from flask import Flask
from flask_restful import Api, Resource, reqparse, output_json


def getThetaValues(overlap: float, daysToOrbit: int) -> List[float]:
    theta = np.ones(5*daysToOrbit)
    value = 0

    for i in range(len(theta)):
        theta[i] = value
        value += (2*np.pi)/daysToOrbit + overlap
        if value >= 2*np.pi:
            value -= 2*np.pi

    theta[-1] = value
    return theta

# def get():
#     t = 2018
#
#     earth_orbit = 1  # AU
#     mars_orbit = 1.524
#     earth_angvel = 2.0e-7  # radians/sec
#     mars_angvel = 1.1e-7
#     current_earth_theta = 0
#     current_mars_theta = 0
#
#     time = np.arange(2018, 10000, 0.01)
#     earth_theta = np.ones(len(time))
#     mars_theta = np.ones(len(time))
#
#     for value in range(len(time)):
#         if value != 0:
#             current_earth_theta = previous_earth_theta + 3.15e5 * earth_angvel
#             current_mars_theta = previous_mars_theta + 3.15e5 * mars_angvel
#         if current_earth_theta >= 2 * np.pi:
#             current_earth_theta -= 2 * np.pi
#         if current_mars_theta >= 2 * np.pi:
#             current_mars_theta -= 2 * np.pi
#
#         earth_theta[value] = current_earth_theta
#         mars_theta[value] = current_mars_theta
#         previous_earth_theta = current_earth_theta
#         previous_mars_theta = current_mars_theta
#
#     return np.concatenate(([time], [earth_theta], [mars_theta]), axis=0)


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


def getOrbitRadiusFromPlanetName(name: str) -> float:
    cur.execute("SELECT OrbitRadius FROM Planets WHERE PlanetName = '" + name + "'")
    result = cur.fetchone()

    return float(result[0])


def getPeriodFromPlanetName(name: str) -> Tuple[str]:
    cur.execute("SELECT PeriodofOrbit FROM Planets WHERE PlanetName = '" + name + "'")
    result = cur.fetchone()

    return int(float(result[0]))


def getAngularVelcityFromPlanetName(name: str) -> float:
    cur.execute("SELECT AngularVelocity FROM Planets WHERE PlanetName = '" + name + "'")
    result = cur.fetchone()

    return float(result[0])


def getAllPlanetNames() -> List[str]:
    cur.execute("SELECT PlanetName from Planets")
    results = cur.fetchall()

    return [name[0] for name in results]


MARS_DIST_SUN= getOrbitRadiusFromPlanetName("Mars")
EARTH_DIST_SUN = getOrbitRadiusFromPlanetName("Earth")
MARS_DAYS_TO_ORBIT = getPeriodFromPlanetName("Mars")
EARTH_DAYS_TO_ORBIT = getPeriodFromPlanetName("Earth")


def convertMarsFromPolar(thetas: List[float]) -> List[float]:
    return [[MARS_DIST_SUN * np.cos(theta), MARS_DIST_SUN * np.sin(theta)] for theta in thetas]


def convertEarthFromPolar(thetas: List[float]) -> List[float]:
    return [[EARTH_DIST_SUN * np.cos(theta), EARTH_DIST_SUN * np.sin(theta)] for theta in thetas]


app = Flask(__name__)
api = Api(app)


class PlanetNames(Resource):
    def get(self):
        return {"planets": getAllPlanetNames()}


class GetMarsPath(Resource):
    def get(self, curYear=2018):
        curOverlap = 0
        if (curYear == 2018):
            curOverlap = 0
        else:
            curOverlap = getThetaValues(curOverlap, EARTH_DAYS_TO_ORBIT)[-1] - 2*np.pi
        times = np.arange(1, 5*EARTH_DAYS_TO_ORBIT + 1)
        xyPairs = convertMarsFromPolar(getThetaValues(curOverlap, EARTH_DAYS_TO_ORBIT))
        marsxs = [p[0] for p in xyPairs]
        marsys = [p[1] for p in xyPairs]
        return {"time": times,
                "marsx": marsxs,
                "marsy": marsys}

@app.route('/GetEarthPath', methods=["GET"])
class GetEarthPath(Resource):
    def get(self, curYear=2018):
        curOverlap = 0
        if (curYear == 2018):
            curOverlap = 0
        else:
            curOverlap = getThetaValues(curOverlap, EARTH_DAYS_TO_ORBIT)[-1] - 2*np.pi
        times = np.arange(1, 5*EARTH_DAYS_TO_ORBIT + 1)
        xyPairs = convertEarthFromPolar(getThetaValues(curOverlap, EARTH_DAYS_TO_ORBIT))
        earthxs = [p[0] for p in xyPairs]
        # earthys = [p[1] for p in xyPairs]
        # print(jsonify({"time": times,
        #         "earthx": earthxs,
        # #         "earthy": earthys}))
        # return jsonify({"time": times,
        #         "earthx": earthxs,
        #         "earthy": earthys})

        return (times, earthxs, earthys)


api.add_resource(PlanetNames, '/PlanetNames')
api.add_resource(GetMarsPath, '/GetMarsPath')
api.add_resource(GetEarthPath, '/GetEarthPath')


if __name__ == "__main__":
    print(getAllPlanetsInit())
    print(getAllRocketNames())
    print(getRocketInfoFromName("Rocket"))
    print(getAllPlanetNames())
    print(getAngularVelcityFromPlanetName("Mars"))
    print(getPeriodFromPlanetName("Mars"))
    print(getOrbitRadiusFromPlanetName("Mars"))
    print(np.arange(1, 5*EARTH_DAYS_TO_ORBIT + 1))
    app.run()

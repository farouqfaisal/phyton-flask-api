from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "api-test"

mysql = MySQL(app)

class location_1(Resource):
    def get(self):
        return {"data" : "this is get method... "}
    def post(self):
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        status = request.form['status']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from location where latitude = %s and longitude = %s and status = %s", [latitude,longitude,status])
        fetchedData = cur.fetchall()

        if len(fetchedData) > 0:
            data = {'name' : fetchedData[0][1], 'status' : fetchedData[0][4], 'message' : 'success'}
        else :
            data = {'message' : 'data not found'}
        return data

class location_2(Resource):
    def get(self):
        return {"data" : "this is get method... "}
    def post(self):
        name = request.form['name']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from location where name = %s", [name])
        fetchedData = cur.fetchall()

        if len(fetchedData) > 0:
            data = {'latitude' : fetchedData[0][2], 'longitude' : fetchedData[0][3], 'message' : 'success'}
        else :
            data = {'message' : 'data not found'}
        return data

api.add_resource(location_1, "/python-api/location-api-1")
api.add_resource(location_2, "/python-api/location-api-2")

if __name__ == "__main__":
    app.run(debug=True)

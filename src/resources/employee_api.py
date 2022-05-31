import json

from flask import current_app, request, jsonify
from flask_restful import Resource

from src.model.employee_dto import Employee


class EmployeeApi(Resource):
    def __init__(self):
        pass


 # jsonify() todo
 # service
 # routes

    def get(self, id=None):
        employee = Employee.objects(id=id)
        return json.loads(employee.to_json()), 200

    def post(self):
        employee_request = request.get_json()
        employee = Employee(**employee_request).save()
        return json.loads(employee.to_json()), 200

    def put(self, id=None):
        return 'Employees'+id

    def delete(self, id=None):
        return 'Employees'+id


class EmployeesApi(Resource):
    def __init__(self):
        pass

    def get(self):
        objects = Employee.objects
        return jsonify(objects)

    def post(self, employee=None):
        return 'Employees'

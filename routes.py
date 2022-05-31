from src.resources.employee_api import EmployeeApi, EmployeesApi


class Routes:

  def initialize_routes(api):
   api.add_resource(EmployeesApi, '/api/v1/employees')
   # api.add_resource(EmployeeApi, '/api/v1/employee')
   api.add_resource(EmployeeApi, '/api/v1/employee/<id>')
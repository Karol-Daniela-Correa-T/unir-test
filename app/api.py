import http.client                 
from flask import Flask            

from app import util               
from app.calc import Calculator, InvalidPermissions   
CALCULATOR = Calculator()          
api_application = Flask(__name__)  
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}   


def execute(operation, *operands):                
    try:                                          
        numbers = [util.convert_to_number(op) for op in operands]   
        return ("{}".format(operation(*numbers)), http.client.OK, HEADERS)   
    except TypeError as e:                         
        return (str(e), http.client.BAD_REQUEST, HEADERS)                   
    except InvalidPermissions as e:                
        return (str(e), http.client.FORBIDDEN, HEADERS)                      


@api_application.route("/")                       
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])   
def add(op_1, op_2):
    return execute(CALCULATOR.add, op_1, op_2)     


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    return execute(CALCULATOR.substract, op_1, op_2)


@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])  
def multiply(op_1, op_2):
    return execute(CALCULATOR.multiply, op_1, op_2)


@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])     
def divide(op_1, op_2):
    return execute(CALCULATOR.divide, op_1, op_2)


@api_application.route("/calc/power/<op_1>/<op_2>", methods=["GET"])      
def power(op_1, op_2):
    return execute(CALCULATOR.power, op_1, op_2)


@api_application.route("/calc/sqrt/<op_1>", methods=["GET"])             
def sqrt(op_1):
    return execute(CALCULATOR.sqrt, op_1)


@api_application.route("/calc/log10/<op_1>", methods=["GET"])            
def log10(op_1):
    return execute(CALCULATOR.log10, op_1)
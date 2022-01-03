
from flask import Flask, request, make_response
from flask_cors import CORS
from openapi_data_generator import OpenApiDataGenerator
from openapi_schema_validator import OAS30Validator
from jsonschema import exceptions
import json

app = Flask("Presentation Generator")
CORS(app)

get_obj_sch = {"type": "object", "properties": {"schema": {"type": "object"}, "endpoint": {"type": "string"},
                                                "method": {"type": "string"}},
               'required': ['schema', 'method', 'endpoint']}

get_all_sch = {"type": "object", "properties": {"schema": {"oneOf": [{"type": "object"}, {'type': "string"}]},
                                                'required': ['schema']}}
local_schema_name = "local_schema.json"


def write_schema(data):
    if isinstance(data, dict):
        with open(local_schema_name, 'w') as f:
            json.dump(data, f, indent=4)
    else:
        with open(local_schema_name, 'w') as f:
            json.dumps(data, indent=4)


@app.route("/")
def hello():
    return "Hello!\nYou can start generate data!\n"


@app.route("/get-object", methods=['POST'])
def get_certain_object():
    try:
        schema_object = OAS30Validator(get_obj_sch)
        schema_object.validate(request.json)
        write_schema(request.json['schema'])
        gen = OpenApiDataGenerator(local_schema_name)
        data = gen.get_random_request_object(request.json['endpoint'], method=request.json['method'])
        return make_response(json.dumps(data), 200)
    except exceptions.ValidationError as e:
        return make_response(json.dumps({'description': 'Request schema is invalid.'}), 400)
    except Exception:
        return make_response(json.dumps({'description': 'Error occurred.'}), 402)


@app.route("/get-all-data", methods=['POST'])
def get_all_data():
    try:
        print(request.json)
        schema_object = OAS30Validator(get_all_sch)
        schema_object.validate(request.json)
        write_schema(request.json['schema'])
        gen = OpenApiDataGenerator(local_schema_name)
        return str(gen)
    except exceptions.ValidationError as e:
        return make_response(json.dumps({'description': 'Request schema is invalid.'}), 400)
    except Exception:
        return make_response(json.dumps({'description': 'Error occurred.'}), 402)


if __name__ == '__main__':
    app.run('0.0.0.0', 1234)


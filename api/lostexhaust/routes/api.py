from lostexhaust import app
from flask import request
from flask import Response
import lostexhaust.config as config
import lostexhaust.util as util
import lostexhaust.data.data_interface as data
import lostexhaust.actions.authentication as authentication
from lostexhaust.models.carpool import Carpool
import json, time

@app.route('/api/person/getinfo/<person_id>.json', methods=['GET'])
def GET_person_info(person_id):
    pass

@app.route('/api/household/info/<household_id>.json', methods=['GET'])
def GET_household_info(household_id):
    token = request.args["token"]
    if authentication.check_token_validity(token, request.remote_addr, int(time.time())):
        resp = data.get_household_from_id(household_id)
        if resp is None:
            return Response(json.dumps({
                "message" : "Invalid household id"
            }), status=400, mimetype="application/json")
        else:
            return Response(resp.serialize(), status=200, mimetype="application/json")
    else:
        return Response(json.dumps({
            "message" : "Invalid token"
        }), status=401, mimetype="application/json")

@app.route('/api/carpool/<household_origin_id>.json', methods=['GET'])
def GET_carpool(household_origin_id):
    token = request.args["token"]
    if authentication.check_token_validity(token, request.remote_addr, int(time.time())):
        target = request.args["target"]
        origin_household = data.get_household_from_id(household_origin_id)
        target_household = data.get_household_from_id(target)
        if origin_household is None or target_household is None:
            return Response(json.dumps({
                "message" : "Invalid household id"
            }), status=400, mimetype="application/json")
        else:
            return Response(Carpool(origin_household.household_id, target_household.household_id, util.geo_distance(origin_household.latitude, origin_household.longitude, target_household.latitude, target_household.longitude)).serialize(), status=200, mimetype="application/json")
    else:
        return Response(json.dumps({
            "message" : "Invalid token"
        }), status=401, mimetype="application/json")

@app.route('/api/carpool/near/<household_origin_id>.json', methods=['GET'])
def GET_carpool_near(household_origin_id):
    token = request.args["token"]
    if authentication.check_token_validity(token, request.remote_addr, int(time.time())):
        if request.args["results"].isdigit():
            num_results = int(request.args["results"])
            origin_household = data.get_household_from_id(household_origin_id)
            other_households = data.get_all_households()
            return json.dumps(util.get_sorted_carpools(origin_household, other_households)[1:num_results+1])
        else:
            return Response(json.dumps({
                "message" : "Invalid number of results"
            }), status=400, mimetype="application/json")
    else:
        return Response(json.dumps({
            "message" : "Invalid token"
        }), status=401, mimetype="application/json")

@app.route('/api/user/info/<user_id>.json', methods=['GET'])
def GET_user_info(user_id):
    pass

@app.route('/api/user/picture/<user_id>.json', methods=['GET'])
def GET_user_picture(user_id):
    pass

@app.route('/api/user/control/<user_id>.json', methods=['PUT'])
def PUT_user_control(user_id):
    pass

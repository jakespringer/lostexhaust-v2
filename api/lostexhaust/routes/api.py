import json, time, os
from lostexhaust import app
from flask import request
from flask import Response
import lostexhaust.config as config
import lostexhaust.util as util
import lostexhaust.data.data_interface as data
import lostexhaust.actions.authentication as authentication
from lostexhaust.models.carpool import Carpool
import logging

ACCESS_CONTROL_ALLOW_ORIGIN = {"Access-Control-Allow-Origin":"*"}

@app.route('/')
def GET_root():
    return "It works!"

@app.route('/person/info/<person_id>.json', methods=['POST'])
def POST_person_info(person_id):
    token = json.loads(request.data)["token"]
    if authentication.check_token_validity(token, request.remote_addr, int(time.time())):
        resp = data.get_people([person_id])
        if len is None or len(resp) != 1:
            return Response(json.dumps({
                "message" : "Invalid person id"
            }), status=400, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
        else:
            return Response(json.dumps(resp[0]), status=200, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
    else:
        return Response(json.dumps({
            "message" : "Invalid token"
        }), status=401, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)


@app.route('/person/everything/<person_id>.json', methods=['POST'])
def POST_person_everything(person_id):
    token = json.loads(request.data)["token"]
    if authentication.check_token_validity(token, request.remote_addr, int(time.time())):
        resp = data.get_people([person_id])
        if len is None or len(resp) != 1:
            return Response(json.dumps({
                "message" : "Invalid person id"
            }), status=400, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
        else:
            households = data.get_households_from_user_id(person_id)
            households_data = map(lambda x: data.get_household_from_id(x[0]).__dict__, households)
            resp[0]['households'] = households_data
            return Response(json.dumps(resp[0]), status=200, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
    else:
        return Response(json.dumps({
            "message" : "Invalid token"
        }), status=401, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)

@app.route('/household/info/<household_id>.json', methods=['POST'])
def POST_household_info(household_id):
    token = json.loads(request.data)["token"]
    if authentication.check_token_validity(token, request.remote_addr, int(time.time())):
        resp = data.get_household_from_id(household_id)
        if resp is None:
            return Response(json.dumps({
                "message" : "Invalid household id"
            }), status=400, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
        else:
            return Response(resp.serialize(), status=200, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
    else:
        return Response(json.dumps({
            "message" : "Invalid token"
        }), status=401, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)

@app.route('/household/everything/<household_id>.json', methods=['POST'])
def POST_household_everything(household_id):
    token = json.loads(request.data)["token"]
    if authentication.check_token_validity(token, request.remote_addr, int(time.time())):
        resp = data.get_household_from_id(household_id)
        if resp is None:
            return Response(json.dumps({
                "message" : "Invalid household id"
            }), status=400, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
        else:
            residents_data = data.get_people(resp.inhabitants)
            resp.inhabitants = residents_data
            return Response(resp.serialize(), status=200, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
    else:
        return Response(json.dumps({
            "message" : "Invalid token"
        }), status=401, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)

@app.route('/carpool/<household_origin_id>.json', methods=['POST'])
def POST_carpool(household_origin_id):
    token = json.loads(request.data)["token"]
    if authentication.check_token_validity(token, request.remote_addr, int(time.time())):
        target = request.args["target"]
        origin_household = data.get_household_from_id(household_origin_id)
        target_household = data.get_household_from_id(target)
        if origin_household is None or tarPOST_household is None:
            return Response(json.dumps({
                "message" : "Invalid household id"
            }), status=400, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
        else:
            return Response(Carpool(origin_household.household_id, target_household.household_id, util.geo_distance(origin_household.latitude, origin_household.longitude, target_household.latitude, target_household.longitude)).serialize(), status=200, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
    else:
        return Response(json.dumps({
            "message" : "Invalid token"
        }), status=401, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)

@app.route('/carpool/near/<household_origin_id>.json', methods=['POST'])
def POST_carpool_near(household_origin_id):
    token = json.loads(request.data)["token"]
    if authentication.check_token_validity(token, request.remote_addr, int(time.time())):
        if request.args["results"].isdigit():
            num_results = int(request.args["results"])
            origin_household = data.get_household_from_id(household_origin_id)
            other_households = data.get_all_households()
            return Response(json.dumps(util.get_sorted_carpools(origin_household, other_households)[1:num_results+1]), status=200, headers=ACCESS_CONTROL_ALLOW_ORIGIN)
        else:
            return Response(json.dumps({
                "message" : "Invalid number of results"
            }), status=400, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
    else:
        return Response(json.dumps({
            "message" : "Invalid token"
        }), status=401, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)

@app.route('/user/info/<user_id>.json', methods=['POST'])
def POST_user_info(user_id):
    pass

@app.route('/person/picture/<user_id>.jpg', methods=['GET'])
def GET_person_picture(user_id):
    token = request.args["token"] if "token" in request.args else ""
    if authentication.check_token_validity(token, request.remote_addr, int(time.time())):
        return Response(data.get_profile_picture(user_id), status=200, mimetype="image/jpeg")
    else:
        return Response("", status=401, mimetype="application/json")

@app.route('/user/control/<user_id>.json', methods=['POST'])
def PUT_user_control(user_id):
    pass

@app.route('/auth/check.json', methods=['GET'])
def GET_auth_check():
    token = request.args["token"]
    if authentication.check_token_validity(token, request.remote_addr, int(time.time())):
        return Response(json.dumps({
            "success" : True,
            "user_id" : authentication.get_person_from_token(token)
        }), status=200, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)
    else:
        return Response(json.dumps({
            "success" : False,
        }), status=200, mimetype="application/json", headers=ACCESS_CONTROL_ALLOW_ORIGIN)

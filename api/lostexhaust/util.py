import math, M2Crypto, base64
from lostexhaust.models.carpool import Carpool
from lostexhaust.models.household import Household

def geo_distance(latitude, longitude, other_latitude, other_longitude):
    lat = math.radians(latitude)
    lon = math.radians(longitude)
    lat2 = math.radians(other_latitude)
    lon2 = math.radians(other_longitude)
    deltaLat = lat2 - lat
    deltaLon = lon2 - lon
    sinPart = (math.sin(deltaLat / 2.0))
    cosPart = (math.cos(lat) * math.cos(lat2) * math.sin(deltaLon / 2.0))
    angle = 2.0 * math.asin(math.sqrt(sinPart * sinPart + cosPart * cosPart))
    return 3960.0 * angle;

def get_sorted_carpools(origin, other_households):
    return sorted([Carpool(origin.household_id, o.household_id, geo_distance(origin.latitude, origin.longitude, o.latitude, o.longitude)).__dict__ for o in other_households], key=lambda e: e["distance"])

def m2crypto_load_der(filename):
    TEMPLATE = """
-----BEGIN RSA PUBLIC KEY-----
%s
-----END RSA PUBLIC KEY-----
"""
    raw = open(filename, 'rb').read()
    data = TEMPLATE % base64.encodestring(raw).rstrip()
    key = M2Crypto.RSA.load_key_string(data)
    return key

def print_file(filename, message):
    with open(filename, 'a') as myfile:
        myfile.write(message + '\n') 

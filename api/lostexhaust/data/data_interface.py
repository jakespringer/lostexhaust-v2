import mysql.connector, urllib2, json
import lostexhaust.config as config
import lostexhaust.util as util
from lostexhaust.models.carpool import Carpool
from lostexhaust.models.household import Household
from lostexhaust.models.person import Person

lookup_table = config.get("sqlLookupTable")
households_table = config.get("sqlHouseholdsTable")

def get_households_from_user_id(person_id):
    cnx = mysql.connector.connect(buffered=True, user=config.get("sqlUsername"), password=config.get("sqlPassword"), host=config.get("sqlHostname"))
    cursor = cnx.cursor()
    query = ("SELECT household_id "
             "FROM " + lookup_table + " "
             "WHERE person_id = %s OR person_id = %s")
    cursor.execute(query, (person_id, person_id))
    result = [household_id for (household_id) in cursor]
    cursor.close()
    cnx.close()
    return result

def get_users_from_household_id(household_id):
    cnx = mysql.connector.connect(buffered=True, user=config.get("sqlUsername"), password=config.get("sqlPassword"), host=config.get("sqlHostname"))
    cursor = cnx.cursor()
    query = ("SELECT person_id "
             "FROM " + lookup_table + " "
             "WHERE household_id = %s OR household_id = %s")
    cursor.execute(query, (household_id, household_id))
    result = [person_id[0] for (person_id) in cursor]
    cursor.close()
    cnx.close()
    return result

def get_household_from_id(household_id):
    cnx = mysql.connector.connect(buffered=True, user=config.get("sqlUsername"), password=config.get("sqlPassword"), host=config.get("sqlHostname"))
    inhabitants = get_users_from_household_id(household_id)
    cursor = cnx.cursor()
    query = ("SELECT place_id, latitude, longitude, addressblock, city, state, postcode "
             "FROM " + households_table + " "
             "WHERE household_id = %s OR household_id = %s")
    cursor.execute(query, (household_id, household_id))
    one = cursor.fetchone()
    if one is None:
        cursor.close()
        cnx.close()
        return None
    else:
        (place_id, latitude, longitude, addressblock, city, state, postcode) = one
        result = Household(household_id, place_id, latitude, longitude, addressblock + " " + city + " " + state + " " + postcode, inhabitants)
        cursor.close()
        cnx.close()
        return result

def get_all_households():
    cnx = mysql.connector.connect(buffered=True, user=config.get("sqlUsername"), password=config.get("sqlPassword"), host=config.get("sqlHostname"))
    cursor = cnx.cursor()
    query = ("SELECT household_id, place_id, latitude, longitude, addressblock, city, state, postcode "
             "FROM " + households_table)
    cursor.execute(query)
    result = [Household(household_id, place_id, latitude, longitude, addressblock + " " + city + " " + state + " " + postcode, None) for (household_id, place_id, latitude, longitude, addressblock, city, state, postcode) in cursor]
    cursor.close()
    cnx.close()
    return result

def get_people(person_id_array):
    url = config.get("catlinApiUrl")
    token = config.get("catlinApiToken")
    response = urllib2.urlopen(url + "?token=" + token + "&query=person&id=" + ",".join(person_id_array)).read()
    return json.loads(response)

def get_profile_picture(person_id):
    url = config.get("catlinPictureUrl")
    token = config.get("catlinPictureToken")
    response = urllib2.urlopen(url + "?token=" + token + "&id=" + person_id)
    return response.read()


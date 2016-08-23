import mysql.connector
import lostexhaust.config as config
from lostexhaust.models.carpool import Carpool
from lostexhaust.models.household import Household
from lostexhaust.models.person import Person

cnx = mysql.connector.connect(user=config.get("sqlUsername"), password=config.get("sqlPassword"), host=config.get("sqlHostname"))

lookup_table = config.get("sqlLookupTable")
households_table = config.get("sqlHouseholdsTable")

def get_households_from_user_id(person_id):
    cursor = cnx.cursor()
    query = ("SELECT household_id "
             "FROM " + lookup_table + " "
             "WHERE person_id = %s OR person_id = %s")
    cursor.execute(query, (person_id, person_id))
    result = [household_id for (household_id) in cursor]
    cursor.close()
    return result

def get_users_from_household_id(household_id):
    cursor = cnx.cursor()
    query = ("SELECT person_id "
             "FROM " + lookup_table + " "
             "WHERE household_id = %s OR household_id = %s")
    cursor.execute(query, (household_id, household_id))
    result = [person_id[0] for (person_id) in cursor]
    cursor.close()
    return result

def get_household_from_id(household_id):
    inhabitants = get_users_from_household_id(household_id)
    cursor = cnx.cursor()
    query = ("SELECT place_id, latitude, longitude, addressblock, city, state, postcode "
             "FROM " + households_table + " "
             "WHERE household_id = %s OR household_id = %s")
    cursor.execute(query, (household_id, household_id))
    one = cursor.fetchone()
    if one is None:
        return None
    else:
        (place_id, latitude, longitude, addressblock, city, state, postcode) = one
        result = Household(household_id, place_id, latitude, longitude, addressblock + " " + city + " " + state + " " + postcode, inhabitants)
        cursor.close()
        return result

def get_all_households():
    cursor = cnx.cursor()
    query = ("SELECT household_id, place_id, latitude, longitude, addressblock, city, state, postcode "
             "FROM " + households_table)
    cursor.execute(query)
    result = [Household(household_id, place_id, latitude, longitude, addressblock + " " + city + " " + state + " " + postcode, None) for (household_id, place_id, latitude, longitude, addressblock, city, state, postcode) in cursor]
    cursor.close()
    return result

# def get_household_hidden(household_id):
#     pass
#
# def get_hidden_households():
#     pass
#
# def get_user_hidden(user_id):
#     pass
#
# def get_hidden_users():
#     pass

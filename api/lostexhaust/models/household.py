import json

class Household:
    household_id = None
    place_id = None
    latitude = 0.0
    longitude = 0.0
    full_address = None
    inhabitants = []

    def __init__(self, household_id, place_id, latitude, longitude, full_address, inhabitants):
        self.household_id = household_id
        self.place_id = place_id
        self.latitude = latitude
        self.longitude = longitude
        self.full_address = full_address
        self.inhabitants = inhabitants

    def serialize(self):
        return json.dumps(self.__dict__)

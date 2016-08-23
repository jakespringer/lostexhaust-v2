import json

class Carpool:
    origin_household_id = None
    target_household_id = None
    distance = 0.0

    def __init__(self, origin_household_id, target_household_id, distance):
        self.origin_household_id = origin_household_id
        self.target_household_id = target_household_id
        self.distance = distance

    def serialize(self):
        return json.dumps(self.__dict__)

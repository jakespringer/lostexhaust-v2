import json

class Person:
    person_id = None
    firstname = None
    lastname = None
    grade_level = None
    class_year = None
    affiliation = None
    opt_out = False
    contact = []
    relationships = []
    homes = []

    def __init__(self, person_id, firstname, lastname, grade_level, class_year, affiliation, opt_out, contact, relationships, homes):
        self.person_id = person_id
        self.firstname = firstname
        self.lastname = lastname
        self.grade_level = grade_level
        self.class_year = class_year
        self.affiliation = affiliation
        self.opt_out = opt_out
        self.contact = contact
        self.relationships = relationships
        self.homes = homes

    def serialize(self):
        return json.dumps(self.__dict__)

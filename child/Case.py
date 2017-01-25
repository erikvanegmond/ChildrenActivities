import time
from calendar import monthrange
from datetime import timedelta, datetime


class Case:
    def __init__(self, case_properties=None):
        if case_properties:
            self.case_properties = case_properties
        else:
            self.case_properties = {}

    def __repr__(self):
        res = ""
        for k, v in self.case_properties.items():
            res += "\t{}".format(k.format(v))
        return res

    def set_property(self, key, value):
        self.case_properties[key] = value

    def get_property(self, key):
        if key in self.case_properties:
            return self.case_properties[key]

    def set_up(self):
        if 'age' not in self.case_properties:
            birth_date_string = input("Birthdate? (dd-mm-yyyy)")
            self.set_property('age_full_date', birth_date_string)
            date = datetime.strptime(birth_date_string, "%d-%m-%Y")
            self.set_property('age', self.monthdelta(date, datetime.now()))

    @staticmethod
    def monthdelta(d1, d2):
        delta = 0
        while True:
            mdays = monthrange(d1.year, d1.month)[1]
            d1 += timedelta(days=mdays)
            if d1 <= d2:
                delta += 1
            else:
                break
        return delta

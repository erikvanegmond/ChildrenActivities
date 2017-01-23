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

from child.Child import Child


class Assessment:
    def __init__(self):
        self.child = Child("Bob")

    def assess_child(self):
        case = self.child.case
        # Loop over the norms
        for norm_name, norm in self.child.norms.norms.items():
            norm.evaluate(case)


    def select_domain(self):
        pass


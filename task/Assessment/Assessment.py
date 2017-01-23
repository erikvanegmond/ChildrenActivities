from child.Child import Child


class Assessment:
    def __init__(self):
        self.child = Child("Bob")

    def assess_child(self):
        case = self.child.case
        # Loop over the norms
        for norm in self.child.norms.selectdomain():
            norm.evaluate(case)


    def select_domain(self):
        pass


from child.Child import Child


class Assessment:
    def __init__(self, child=None):
        if child:
            self.child = child
        else:
            self.child = Child()

    def assess_child(self):
        case = self.child.case
        # Loop over the norms
        for norm in self.child.norms.select_domain():
            norm.evaluate(case)


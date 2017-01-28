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

    def decide_focus_norm(self):
        focus = (None, "")
        for norm in self.child.norms.norms:

            score = self.child.norms.norms[norm].norm_score
            if focus[0] is None or focus[0] > score:
                focus = (score, norm)
        return focus


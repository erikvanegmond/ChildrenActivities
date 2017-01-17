from child.Case import Case
from task.Assessment.Norms import Norms


class Child:
    def __init__(self, name=None):
        if name is None:
            self.name = input("Name of the child: ")
        else:
            self.name = name

        self.case = Case()
        self.norms = Norms()
        self.norms.set_case(self.case)


    def __repr__(self):
        return "Child({})".format(self.name)

    def __str__(self):
        return "Child({})\n{}\n{}\n".format(self.name, self.case, self.norms)

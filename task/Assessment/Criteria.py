class Criteria:
    pass


class Criterium(Criteria):
    case = None

    def __init__(self, criterium, norm_score=None, parent_criterium=None):
        self.criterium = criterium
        self.norm_score = norm_score
        self.parent_criterium = parent_criterium

    def make_question(self, filler):
        return self.criterium.format(filler) + "?\n"

    def ask(self):
        answer = None
        while True:
            try:
                answer = int(input(self.make_question("any")))
                break
            except ValueError:
                continue
        return answer

    def evaluate(self, case_value: object) -> int:
        pass

    def set_case(self, new_case):
        Criterium.case = new_case


class CountCriterium(Criterium):
    def __init__(self, criterium, count, norm_score=None, parent_criterium=None):
        super().__init__(criterium, norm_score, parent_criterium)
        self.count = count

    def __repr__(self):
        return self.criterium.format(self.count)

    def __str__(self):
        return self.criterium.format(self.count)

    def ask(self):
        answer = None
        while True:
            try:
                answer = int(input(self.make_question("how many")))
                break
            except ValueError:
                continue
        return answer

    def evaluate(self, case_value: object) -> int:
        if case_value >= self.count:
            return self.norm_score


class BooleanCriterium(Criterium):
    """
    Can child do x? {}
    """

    true_list = ['true', 'y', '1']
    false_list = ['false', 'n', '0']

    def __init__(self, criterium, boolean, norm_score=None, parent_criterium=None):
        super().__init__(criterium, norm_score, parent_criterium)
        self.boolean = boolean

    def __repr__(self):
        return self.criterium.format(self.boolean)

    def __str__(self):
        return self.criterium.format(self.boolean)

    def ask(self):
        answer = None
        while True:
            string_input = str(input(self.make_question("True/False"))).lower()
            if string_input in self.true_list:
                answer = True
            elif string_input in self.false_list:
                answer = False
            else:
                continue
            break
        if answer == self.boolean and self.parent_criterium is not None:
            for parent in self.parent_criterium:
                self.case.set_property(parent.criterium, parent.boolean)

        return answer

    def evaluate(self, case_value: object) -> int:
        if case_value == self.boolean:
            return self.norm_score

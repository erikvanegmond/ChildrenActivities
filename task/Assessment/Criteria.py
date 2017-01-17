class Criteria:
    pass


class Criterium(Criteria):
    def __init__(self, criterium, norm_score):
        self.criterium = criterium
        self.norm_score = norm_score

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


class CountCriterium(Criterium):
    def __init__(self, criterium, count, norm_score):
        super().__init__(criterium, norm_score)
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
    def __init__(self, criterium, boolean, norm_score):
        super().__init__(criterium, norm_score)
        self.boolean = boolean

    def __repr__(self):
        return self.criterium.format(self.boolean)

    def __str__(self):
        return self.criterium.format(self.boolean)

    def ask(self):
        answer = None
        while True:
            try:
                answer = int(input(self.make_question("True/False")))
                break
            except ValueError:
                continue
        return answer

    def evaluate(self, case_value: object) -> int:
        if case_value == self.boolean:
            return self.norm_score

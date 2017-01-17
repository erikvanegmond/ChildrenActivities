from task.Assessment.Criteria import *


class Norm:
    """
    Norms are measured in months
    """

    def __init__(self):
        self.normCriteria = list()
        self.norm_score = 0

    def __repr__(self):
        return "[" + ",".join(map(str, self.normCriteria)) + "]"

    def evaluate(self, case):
        # Loop over the criteria for the norm
        for criterium in self.norm_criteria_prioritizer():
            criterium_str = criterium.criterium

            if criterium.parent_criterium is not None:
                # for parent in criterium.parent_criterium:
                #     if parent.criterium is criterium_str:
                #         print("hi")

                new_case_properties = {}
                for case_prop in case.case_properties.keys():
                    if case_prop is criterium_str:
                        for parent in criterium.parent_criterium:
                            new_case_properties[parent.criterium] = parent.boolean
                if new_case_properties:
                    for k, v in new_case_properties.items():
                        case.set_property(k, v)

            # check criterium with case
            if criterium_str not in case.case_properties:
                property_value = criterium.ask()
                case.set_property(criterium_str, property_value)
            else:
                property_value = case.get_property(criterium_str)

            # Get the score for this criterium
            score = criterium.evaluate(property_value)

            if score is not None:
                # TODO: a better approach for the norm score
                # If the score is better than before, override it
                self.norm_score = max(score, self.norm_score)

    def norm_criteria_prioritizer(self):
        for i in self.normCriteria:
            yield i


class LanguageProductionNorm(Norm):
    def __init__(self):
        super().__init__()
        self.normCriteria.append(CountCriterium("Can speak {} words", 2, 12))
        self.normCriteria.append(CountCriterium("Can speak {} words", 10, 24))
        self.normCriteria.append(BooleanCriterium("Child can use 3 different vowels? {}", True, 4,
                                                  parent_criterium=[BooleanCriterium("Child can use 2 different vowels? {}", True)]))
        self.normCriteria.append(BooleanCriterium("Child can use 2 different vowels? {}", True, 3,
                                                  parent_criterium=[BooleanCriterium("Child can vocalize? {}", True)]))
        self.normCriteria.append(BooleanCriterium("Child can vocalize? {}", True, 0))


class LanguageComprehensionNorm(Norm):
    def __init__(self):
        super().__init__()


class SocialSkillsNorm(Norm):
    def __init__(self):
        super().__init__()


class GrossMotorSkillsNorm(Norm):
    def __init__(self):
        super().__init__()


class FineMotorSkillsNorm(Norm):
    def __init__(self):
        super().__init__()


class Norms:
    norms = {"LanguageProductionNorm": LanguageProductionNorm(),
             "LanguageComprehensionNorm": LanguageComprehensionNorm(),
             "SocialSkillsNorm": SocialSkillsNorm(),
             "GrossMotorSkillsNorm": GrossMotorSkillsNorm(),
             "FineMotorSkillsNorm": FineMotorSkillsNorm()}

    def __init__(self):
        pass

    def __repr__(self):
        res = ""
        for norm_name, norm in self.norms.items():
            res += "\t{}:{}\n".format(norm_name, norm.norm_score)
        return res

    def set_case(self, case):
        self.norms["LanguageProductionNorm"].normCriteria[0].set_case(case)

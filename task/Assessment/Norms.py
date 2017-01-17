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
        for criterium in self.normCriteria:
            criterium_str = criterium.criterium

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


class LanguageProductionNorm(Norm):
    def __init__(self):
        super().__init__()
        self.normCriteria.append(CountCriterium("Can speak {} words", 2, 12))
        self.normCriteria.append(CountCriterium("Can speak {} words", 4, 15))
        self.normCriteria.append(CountCriterium("Can speak {} words", 6, 18))
        self.normCriteria.append(CountCriterium("Can speak {} words", 25, 20))
        self.normCriteria.append(CountCriterium("Can speak {} words", 50, 30))
        self.normCriteria.append(CountCriterium("Can speak {} words", 200, 36))

        self.normCriteria.append(BooleanCriterium("Child can vocalize without crying? {}", True, 1))
        self.normCriteria.append(BooleanCriterium("Child can use one vowel {}", True, 1))
        self.normCriteria.append(BooleanCriterium("Child reacts with body movements upon talking {}", True, 1))
        self.normCriteria.append(BooleanCriterium("Child makes soft noise upon talking {}", True, 2))
        self.normCriteria.append(BooleanCriterium("Child can use 2 different vowels? {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child brabbles {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child can laugh out loud {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child vocalizes in different ways {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child tries to imitate adults {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child tries to imitate 'talking' {}", True, 3))
        self.normCriteria.append(
            BooleanCriterium("Child combines vowels and consonants to make ba/da structures {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child can make at least 4 different sounds' {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child uses repeatable 2-syllable structures baba/dada {}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child can use sounds to take its turn {}", True, 6))
        self.normCriteria.append(BooleanCriterium(
            "Child screams for attention and protests if by loud noise or crying something  happens that he/she dislikes {}",
            True, 6))
        self.normCriteria.append(BooleanCriterium("Child can imitate movements and sounds {}", True, 6))
        self.normCriteria.append(
            BooleanCriterium("Child smiles and vocalizes when meeting a faimliar person {}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child can use intonation patterns similar to adults {}", True, 9))
        self.normCriteria.append(
            BooleanCriterium("Child can imitate face movements in combination with sounds {}", True, 9))
        self.normCriteria.append(BooleanCriterium(
            "Child vocalizes interactively and makes use of voice inflections as well as objects during interaction {}",
            True, 12))
        self.normCriteria.append(
            BooleanCriterium("Child uses consistent same sounds for leaving/arriving {}", True, 12))
        self.normCriteria.append(BooleanCriterium("Child reacts in (semi) words to simple questions  {}", True, 12))
        self.normCriteria.append(
            BooleanCriterium("Child uses adult intonation pattern including questions and exclamations  {}", True, 12))
        self.normCriteria.append(BooleanCriterium("Child tries to sing along with songs {}", True, 15))
        self.normCriteria.append(BooleanCriterium("Child is a good imitator and repeats words of adults {}", True, 15))
        self.normCriteria.append(
            BooleanCriterium("Child uses words for persons, objects, animals and 'no' {}", True, 15))
        self.normCriteria.append(BooleanCriterium(
            "Child uses consistent words for leaving/arriving/greeting and is able to describe movements with >2words {}",
            True, 18))



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

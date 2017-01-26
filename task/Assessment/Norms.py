from collections import defaultdict

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

    def norm_criteria_prioritizer(self, case=None):
        if not case:
            for i in self.normCriteria:
                yield i
        else:
            # too complicated for now. :(
            age = case.get_property('age')
            criteria_by_age = defaultdict(list)
            for criterium in self.normCriteria:
                criteria_by_age[criterium.norm_score].append(criterium)
            ages = sorted(list(criteria_by_age.keys()))
            check_age = min(ages, key=lambda x: abs(x-age))
            continue_checking = True
            while continue_checking:
                criteria = list(criteria_by_age[check_age])
                while criteria:
                    yield criteria.pop()


# ToDO child prioritizer
# TODO after 4x False stop questions

class LanguageProductionNorm(Norm):
    def __init__(self):
        super().__init__()
        self.normCriteria.append(BooleanCriterium("Child can use 3 different vowels? {}", True, 4,
                                                  parent_criterium=[
                                                      BooleanCriterium("Child can use 2 different vowels? {}", True)]))

        self.normCriteria.append(BooleanCriterium("Child can use 2 different vowels? {}", True, 3,
                                                  parent_criterium=[BooleanCriterium("Child can vocalize? {}", True)]))

        self.normCriteria.append(BooleanCriterium("Child can imitate two-word-sentences {}", True, 18,
                                                  parent_criterium=[BooleanCriterium(
                                                      "Child is a good imitator and repeats words of adults {}", True),
                                                      (BooleanCriterium(
                                                          "Child can imitate movements and sounds {}",
                                                          True))]))

        self.normCriteria.append(BooleanCriterium("Child is a good imitator and repeats words of adults {}", True, 15,
                                                  parent_criterium=[
                                                      BooleanCriterium("Child can imitate movements and sounds {}",
                                                                       True)]))

        self.normCriteria.append(BooleanCriterium("Child uses repeatable 2-syllable structures baba/dada {}", True, 6,
                                                  parent_criterium=[
                                                      BooleanCriterium("Child can use 2 different vowels? {}", True)]))

        self.normCriteria.append(BooleanCriterium("Child uses adult-like intonation {}", True, 36,
                                                  parent_criterium=[BooleanCriterium(
                                                      "Child can use intonation patterns similar to adults {}", True),
                                                      (BooleanCriterium(
                                                          "Child uses adult intonation pattern including questions and exclamations  {}",
                                                          True))]))

        self.normCriteria.append(BooleanCriterium("Child can answer many questions{}", True, 36,
                                                  parent_criterium=[BooleanCriterium(
                                                      "Child reacts in (semi) words to simple questions  {}", True)]))

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
        self.normCriteria.append(BooleanCriterium("Child can imitate two-word-sentences {}", True, 18))
        self.normCriteria.append(
            BooleanCriterium("Child's speech is understandable for at least 2/3 of time {}", True, 18))
        self.normCriteria.append(BooleanCriterium("Child can use 3 word-sentences {}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child takes turn in conversations {}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child starts to understand basic grammar {}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child can say a child rhyme{}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child asks w'questions like where, what {}", True, 30))
        self.normCriteria.append(BooleanCriterium("Child can talk about experiences {}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child can say its full name {}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child can answer many questions{}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child can sing simple songs {}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child can whisper and scream {}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child can repeat a 6 word sentence {}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child uses adult-like intonation {}", True, 36))


class LanguageComprehensionNorm(Norm):
    def __init__(self):
        super().__init__()

        self.normCriteria.append(BooleanCriterium("Child reacts at noise {}", True, 1))
        self.normCriteria.append(BooleanCriterium("Child looks at face for a while {}", True, 1))
        self.normCriteria.append(BooleanCriterium("Child had interest in surrounding{}", True, 2))
        self.normCriteria.append(BooleanCriterium("Child searches with eyes where sound is coming from {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child turns in movement of sound/voice {}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child sits quiet in chair and has attention for object {}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child can look at image for 2 minutes {}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child changes facial expression in reaction to mad/friendly voices {}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child listens to 1 talking person in noisy environment {}", True, 9))
        self.normCriteria.append(BooleanCriterium("Child reacts to own name {}", True, 9))
        self.normCriteria.append(BooleanCriterium("Child can point to specific object {}", True, 12))
        self.normCriteria.append(BooleanCriterium("Child listens to short story {}", True, 18))
        self.normCriteria.append(BooleanCriterium("Child listens to 10-min story {}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child answers during story simple questions {}", True, 36))

class SocialSkillsNorm(Norm):
    def __init__(self):
        super().__init__()

        self.normCriteria.append(CountCriterium("Can follow orders {} percent of time", 50, 24))
        self.normCriteria.append(CountCriterium("Can follow orders {} percent of time", 75, 36))

        self.normCriteria.append(BooleanCriterium("Child is quiet after picking up {}", True, 1))
        self.normCriteria.append(BooleanCriterium("Child looks shortly at face {}", True, 1))
        self.normCriteria.append(BooleanCriterium("Child smiles or makes noice after talking {}", True, 1))
        self.normCriteria.append(BooleanCriterium("Child brings toy/object to mouth {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child expects to be lifted by i.e. moving limbs {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child smiles spontaneously {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child recognizes drinking bottle {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child plays with hands and clothes{}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child smiles at mirror image{}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child tries to grab piece of toy outside arm reach{}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child smiles if piece of cloth is put on head {}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child smiles at familiar game {}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child plays with feet {}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child reacts on presence strangers by staring/crying {}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child plays with different sorts of toys for 10min {}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child joins with playing kiekeboe {}", True, 9))
        self.normCriteria.append(BooleanCriterium("Child plays simple games together {}", True, 9))
        self.normCriteria.append(BooleanCriterium("Child plays simple functional games {}", True, 9))
        self.normCriteria.append(BooleanCriterium("Child plays with ball by pushing it back {}", True, 9))
        self.normCriteria.append(BooleanCriterium("Child plays 15-20min alone without adult {}", True, 9))
        self.normCriteria.append(BooleanCriterium("Child often throws with toy if it doesn't want it {}", True, 12))
        self.normCriteria.append(BooleanCriterium("Child tries shows off to get attention of parents {}", True, 12))
        self.normCriteria.append(BooleanCriterium("Child helps with putting on simple clothes {}", True, 12))
        self.normCriteria.append(BooleanCriterium("Child shows toy to adult {}", True, 12))
        self.normCriteria.append(BooleanCriterium("Child turns image/book with correct side up to itself {}", True, 15))
        self.normCriteria.append(BooleanCriterium("Child imitates domestic work {}", True, 15))
        self.normCriteria.append(BooleanCriterium("Child plays in meaningful manner {}", True, 15))
        self.normCriteria.append(BooleanCriterium("Child can communicate with friends with signs {}", True, 18))
        self.normCriteria.append(BooleanCriterium("Child looks at other children playing {}", True, 18))
        self.normCriteria.append(BooleanCriterium("Child defends own toys {}", True, 18))
        self.normCriteria.append(BooleanCriterium("Child helps with simple domestic work {}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child plays with dolls {}", True, 24))
        self.normCriteria.append(
            BooleanCriterium("Child plays next to other children and is in contact with them {}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child makes choices if asked {}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child waits for its own turn {}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child listens to music/story for 10min {}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child says please if reminded {}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child joins with songs/rhymes{}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child can say goodbye to parents without crying{}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child keeps to the rules of a game under guidance{}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child waits for its turn with other children{}", True, 36))
        self.normCriteria.append(
            BooleanCriterium("Child says half of the time please and thankyou without reminder{}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child knows own gender and can name it{}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child does simple domestic work tasks{}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child avoids danger{}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child stays within clear rules of parents{}", True, 36))
        self.normCriteria.append(BooleanCriterium("Child can share attention of parents{}", True, 36))


class GrossMotorSkillsNorm(Norm):
    def __init__(self):
        super().__init__()
        self.normCriteria.append(BooleanCriterium("Child can raise head{}", True, 1))
        self.normCriteria.append(BooleanCriterium("Child's head balance is stable{}", True, 4))
        self.normCriteria.append(BooleanCriterium("Child's posture is symmetrical{}", True, 4))
        self.normCriteria.append(BooleanCriterium("Child can stand with support{}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child can sit without support{}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child can walk with support{}", True, 12))
        self.normCriteria.append(BooleanCriterium("Child can walk without support{}", True, 18))
        self.normCriteria.append(BooleanCriterium("Child sit without support{}", True, 18))
        self.normCriteria.append(BooleanCriterium("Child can jump{}", True, 36))

class FineMotorSkillsNorm(Norm):
    def __init__(self):
        super().__init__()
        self.normCriteria.append(BooleanCriterium("Child can make fist {}", True, 1))
        self.normCriteria.append(BooleanCriterium("Child can follow something with eyes{}", True, 3))
        self.normCriteria.append(BooleanCriterium("Child can move object {}", True, 6))
        self.normCriteria.append(BooleanCriterium("Child can staple 2 blocks {}", True, 12))
        self.normCriteria.append(BooleanCriterium("Child can doodle with pencil {}", True, 18))
        self.normCriteria.append(BooleanCriterium("Child can turn pages {}", True, 18))
        self.normCriteria.append(BooleanCriterium("Child can draw a circle{}", True, 24))
        self.normCriteria.append(BooleanCriterium("Child can staple 10 blocks{}", True, 36))

class Norms:
    norms = {"LanguageProductionNorm": LanguageProductionNorm(),
             "LanguageComprehensionNorm": LanguageComprehensionNorm(),
             "SocialSkillsNorm": SocialSkillsNorm(),
             "GrossMotorSkillsNorm": GrossMotorSkillsNorm(),
             "FineMotorSkillsNorm": FineMotorSkillsNorm()}

    def __init__(self):
        pass

    def select_domain(self):
        domain_list = ["LanguageProductionNorm", "LanguageComprehensionNorm", "SocialSkillsNorm",
                       "GrossMotorSkillsNorm", "FineMotorSkillsNorm"]
        for domain in domain_list:
            yield self.norms[domain]

    def __repr__(self):
        res = ""
        for norm_name, norm in self.norms.items():
            res += "\t{}:{}\n".format(norm_name, norm.norm_score)
        return res

    def set_case(self, case):
        self.norms["LanguageProductionNorm"].normCriteria[0].set_case(case)

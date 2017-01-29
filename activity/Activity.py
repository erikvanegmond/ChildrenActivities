import random


class ActivityPlanner:
    def __init__(self, goal=None, assessed_age=0):
        self.goal = goal
        self.activityComponents = []
        self.batch_number = 20

        self.requirements = {
            'location': {'value': 'inside', 'soft-hard': "soft", 'type': str},
            'age': {'value': assessed_age, 'soft-hard': "hard", 'type': int}
        }

    def run(self):
        activities = []
        for _ in range(self.batch_number):
            act = Activity(goal=self.goal)
            act.generate()

            activities.append(act)

        activities = self.select_subset(activities)
        acts = [[act, self.count_soft_violations(act)] for act in activities]
        activities = sorted(activities, key=lambda x: self.count_soft_violations(x))
        build_activities = []
        for activity in activities:
            build_activities.append(activity.build())

        def filter_unique(seq):
                seen = set()
                seen_add = seen.add
                return [x for x in seq if not (x in seen or seen_add(x))]
        self.propose(filter_unique(build_activities))

    @staticmethod
    def propose(build_activities):
        for activity in build_activities:
            print(activity)

    def check_component(self, component_config, check_soft_hard=True):
        def check_constraint(constraint, constraint_value, self, check_soft_hard = True):

            for requirement, value in self.requirements.items():
                if not check_soft_hard or value['soft-hard'] == 'hard':
                    if value['type'] == str and \
                                    requirement == constraint and constraint_value != value['value']:
                        return False
                    if value['type'] == int and (
                            constraint in ["min_age", "max_age"] and requirement == "age"):
                        if constraint == "min_age" and constraint_value > value['value']:
                            return False
                        if constraint == "max_age" and constraint_value < value['value']:
                            return False
            return True

        for key, value in component_config.items():
            if type(value) is dict:
                return self.check_component(value)
            else:
                # print(key, value)
                if key == "class":
                    for constraint, constraint_value in value.properties.items():
                        res = check_constraint(constraint, constraint_value, self, check_soft_hard)
                        if not res:
                            return False
                else:
                    return check_constraint(key, value, self, check_soft_hard)
        return True

    def select_subset(self, activities):
        subset = []
        for activity in activities:
            skipped = False
            for component in activity.activity:
                if not self.check_component(component[1]):
                    print("skip", activity.activity)
                    skipped = True
                    break
                if not self.check_component(component[0].properties):
                    print("skip", activity.activity)
                    skipped = True
                    break
            if not skipped:
                subset.append(activity)
                skipped = False
        return subset

    def count_soft_violations(self, activity):
        violations = 0
        for component in activity.activity:
            if not self.check_component(component[1]):
                violations += 1
            if not self.check_component(component[0].properties, check_soft_hard=False):
                violations += 1
        return violations


class Activity:
    def __init__(self, goal=None):
        self.activity = []
        self.goal = goal
        self.activityComponents = []

    def __repr__(self):
        return "Activity({})".format(self.goal)

    def generate(self):
        if self.goal in ActivityComponentsCatalog.catalog:
            component_list = ActivityComponentsCatalog.catalog[self.goal]
            # pick random activity to work on the goal
            component = random.choice(component_list)
            activity_config = self.configure_activity_component(component)
            self.activity.append((component, activity_config))

    def build(self):
        for component in self.activity:
            activity_component = component[0]
            config = component[1]
            activity_component_applied = activity_component().apply_config(config)
            return "{}".format(activity_component_applied)

    def configure_activity_component(self, activity_component):
        needs = activity_component.needs
        activity_config = {}
        for need in needs:
            activity_config = {}
            if type(need) is str:
                config = self.pull_from_object_catalog([need])
                return config
            elif type(need) is tuple:
                name = need[0]
                the_need = need[1]
                activity_component_config = self.parse_list_needs_to_config(the_need)
                activity_config[name] = activity_component_config
            else:
                activity_component = need()
        return activity_config

    def parse_list_needs_to_config(self, the_need):
        picked_need = random.choice(the_need)
        activity_component = picked_need()
        activity_component_config = self.pull_from_object_catalog(activity_component.needs)
        activity_component_config['class'] = picked_need
        return activity_component_config

    @staticmethod
    def pull_from_object_catalog(needs):
        config = None
        while config is None:
            config = random.choice(ObjectCatalog.catalog)
            for need in needs:
                if need not in config:
                    config = None
                    break
        return config


class ActivityComponent:
    template = ""
    needs = []
    properties = {}

    def print_components(self):
        for config in self.configs:
            print(self.template.format(**config))

    def generate(self):
        conf = random.choice(self.configs)
        return self.template.format(**conf)

    def iterate_configs(self):
        for config in self.configs:
            yield self.template.format(**config)

    def apply_config(self, config={}):
        if 'activity_config' in config:
            activity_config = config['activity_config']
            config['activity_config_settings'] = config['activity_config']
            if 'class' in activity_config:
                activity_component = activity_config['class']()
                config['activity_config'] = activity_component.apply_config(config=activity_config)
        return self.template.format(**config)

    def __repr__(self):
        return "ActivityComponent(\"{}\")".format(self.template)


class ColorNamingActivityComponent(ActivityComponent):
    template = "name the color of the {object}"
    needs = ["object"]


class DescribingObjectActivityComponent(ActivityComponent):
    template = "describe the following {object}"
    needs = ["object"]


class BuildActivityComponent(ActivityComponent):
    needs = ['activity', 'activity_result', 'object']
    template = "{activity} a {activity_result} by adding a {object} to the {activity_result}"


class VerbNounActivityComponent(ActivityComponent):
    needs = ['object', 'no_result', 'activity']
    template = "{activity} the {object}"


class TakeTurnsActivityComponent(ActivityComponent):
    template = "take turns, child do {activity_config}, you do {activity_config}"
    needs = [('activity_config', [
        ColorNamingActivityComponent,
        BuildActivityComponent,
        VerbNounActivityComponent
    ])]


class HideAndSeekActivityComponent(ActivityComponent):
    needs = ['object', 'no_result']
    template = "play hide and seek with {object}"
    properties = {'location': 'outside'}


class FixedSocialskillsActivityComponent(ActivityComponent):
    template = "{fixed_sentence_social}"
    needs = ["fixed_sentence_social"]


class FixedLanguageComprehensionskillsActivityComponent(ActivityComponent):
    template = "{fixed_sentence_language_comprehension}"
    needs = ["fixed_sentence_language_comprehension"]


class FixedLanguageProductionActivityComponent(ActivityComponent):
    template = "{fixed_sentence_language_production}"
    needs = ["fixed_sentence_language_production"]


class FixedGrossMotorActivityLComponent(ActivityComponent):
    template = "{fixed_sentence_gross_motor}"
    needs = ["fixed_sentence_gross_motor"]


class FixedFineMotorActivityLComponent(ActivityComponent):
    template = "{fixed_sentence_fine_motor}"
    needs = ["fixed_sentence_fine_motor"]


class ActivityComponentsCatalog:
    catalog = {"LanguageProductionNorm": [TakeTurnsActivityComponent, ColorNamingActivityComponent,
                                          DescribingObjectActivityComponent],
               "SocialSkillsNorm": [TakeTurnsActivityComponent, FixedSocialskillsActivityComponent,
                                    HideAndSeekActivityComponent],
               "LanguageComprehensionNorm": [FixedLanguageComprehensionskillsActivityComponent,
                                             DescribingObjectActivityComponent],
               "FineMotorSkillsNorm": [FixedFineMotorActivityLComponent],
               "GrossMotorSkillsNorm": [FixedGrossMotorActivityLComponent]
               }


class ObjectCatalog:
    catalog = [
        {"object": "cloth", "activity": "drop", "no_result": True, 'max_age': 18},
        {"object": "car", "activity": "drop", "no_result": True},
        {"object": "block", "activity": "build", "activity_result": "towers"},
        {"object": "train track", "activity": "build", "activity_result": "train track", 'min_age': 24},
        {"object": "block", "activity": "drop", "no_result": True, 'max_age': 18},
        {"object": "daddy", "activity": "tickle", "no_result": True, 'max_age': 24},
        {"object": "sand", "activity": "hit", "no_result": True, 'location': 'outside', 'max_age': 18},
        {"object": "door", "activity": "knock", "no_result": True, 'max_age': 18},
        {"object": "piano", "activity": "play", "no_result": True, 'min_age': 18},
        {"object": "cake-mix", "activity": "mix", "no_result": True, 'min_age': 18},
        {"object": "clothing"},
        {"object": "puzzle piece"},
        {"object": "thing around you"},
        {"fixed_sentence_social": "do domestic work activities together", 'min_age': 18},
        {"fixed_sentence_social": "practice saying please & thankyou", 'min_age': 30},
        {"fixed_sentence_social": "ask child to choose from variety of toys", 'min_age': 18},
        {"fixed_sentence_social": "play kiekeboe", 'max_age': 24},
        {"fixed_sentence_social": "smile and laugh to your child ", 'max_age': 12},
        {"fixed_sentence_language_comprehension": "talk about everything you do, 'subtitle'"},
        {"fixed_sentence_language_comprehension": "show different objects to child and talk about it, 'subtitle'"},

    ]


"""
* Color naming
* puzzle
* games
* drawing
* naming things
* hide and seek
* reading
* take turns eating
"""

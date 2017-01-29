import random


class ActivityPlanner:
    def __init__(self, goal=None, assessed_age=0):
        self.goal = goal
        self.activityComponents = []
        self.age = assessed_age
        self.batch_number = 10

    def run(self):
        activities = []
        build_activities = []
        for _ in range(self.batch_number):
            act = Activity(goal=self.goal, assessed_age=self.age)
            act.generate()

            activities.append(act)
            build_activities.append(act.build())
        self.propose(set(build_activities))

    @staticmethod
    def propose(build_activities):
        for activity in build_activities:
            print(activity)


class Activity:
    def __init__(self, goal=None, assessed_age=0):
        self.activity = []
        self.goal = goal
        self.activityComponents = []
        self.age = assessed_age

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


class FixedActivityComponent(ActivityComponent):
    template = "this is fixed"
    needs = []

class ActivityComponentsCatalog:
    catalog = {"LanguageProductionNorm": [TakeTurnsActivityComponent, ColorNamingActivityComponent],
               "SocialSkillsNorm": [TakeTurnsActivityComponent, FixedActivityComponent]
               }


class ObjectCatalog:
    catalog = [
        {"object": "cloth", "activity": "drop", "no_result": True, 'max_age': 18},
        {"object": "car", "activity": "drop", "no_result": True},
        {"object": "block", "activity": "build", "activity_result": "towers"},
        {"object": "train track", "activity": "build", "activity_result": "train track", 'min_age':24},
        {"object": "block", "activity": "drop", "no_result": True, 'max_age': 18},
        {"object": "daddy", "activity": "tickle", "no_result": True, 'max_age': 24},
        {"object": "sand", "activity": "hit", "no_result": True, 'location': 'outside', 'max_age': 18},
        {"object": "door", "activity": "knock", "no_result": True, 'max_age': 18},
        {"object": "piano", "activity": "play", "no_result": True, 'min_age': 18},
        {"object": "cace-ix", "activity": "mix", "no_result": True, 'min_age': 18},
        {"object": "clothing"},
        {"object": "puzzle piece"},
        {"object": "thing around you"},
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

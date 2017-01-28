import random


class ActivityPlanner:
    def __init__(self, goal=None, assessed_age=0):
        self.goal = goal
        self.activityComponents = []
        self.age = assessed_age
        self.batch_number = 10

    def run(self):
        activities = []
        for _ in range(self.batch_number):
            act = Activity(goal=self.goal, assessed_age=self.age)
            act.generate()
            act.build()
            print(act.activity)
            activities.append(act)
        # for a in activities:
        #     # print(a.activity)
        #

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
            print("::{}".format(activity_component_applied))

    def configure_activity_component(self, activity_component):
        needs = activity_component.needs
        for need in needs:
            activity_config = {}
            if type(need) is str:
                config = self.pull_from_object_catalog([need])
                return config
            elif type(need) is list:
                pass
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
            if 'class' in activity_config:
                activity_component = activity_config['class']()
                config['activity_config'] = activity_component.apply_config(config=activity_config)
        return self.template.format(**config)

    def __repr__(self):
        return "ActivityComponent(\"{}\")".format(self.template)


class ColorNamingActivityComponent(ActivityComponent):
    template = "name the color of the {object}"
    needs = ["object"]
    configs = [
        {"object": "cloth"},
        {"object": "car"},
        {"object": "block"},
        {"object": "clothing"},
        {"object": "puzzle piece"},
        {"object": "thing around you"},
    ]


class BuildActivityComponent(ActivityComponent):
    needs = ['activity', 'activity_result', 'object']
    template = """{activity} a {activity_result} by adding a {object} to the {activity_result}. """


class TakeTurnsActivityComponent(ActivityComponent):
    template = "take turns, child do {activity_config}, you do {activity_config}"
    needs = [('activity_config', [ColorNamingActivityComponent, BuildActivityComponent])]


class ActivityComponentsCatalog:
    catalog = {"LanguageProductionNorm": [TakeTurnsActivityComponent, ColorNamingActivityComponent],
               "SocialSkillsNorm": [TakeTurnsActivityComponent],
               "taking turns": [TakeTurnsActivityComponent],
               "colors": [ColorNamingActivityComponent]}


class ObjectCatalog:
    catalog = [
        {"object": "cloth"},
        {"object": "car"},
        {"object": "block", "activity": "build", "activity_result": "towers"},
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

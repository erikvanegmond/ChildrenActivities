class ActivityComponentsCatalog:
    catalog = {""}


class Activity:
    def __init__(self, goal=None):
        self.goal = goal
        self.activityComponents = []

    def __repr__(self):
        return "Activity({})".format(self.goal)


class ActivityComponent:
    template = ""
    configs = []

    def print_components(self):
        for config in self.configs:
            print(self.template.format(**config))

    pass


class BuildActivityComponent(ActivityComponent):
    template = """Start {activity} a {activity_result} by {goal} to add a {object} to the {activity_result}. """
    configs = [
        {
            "object": "blocks",
            "activity": "building",
            "goal": "taking turns",
            "activity_result": "tower"
        }, {
            "object": "train tracks pieces",
            "activity": "building",
            "goal": "taking turns",
            "activity_result": "train track"
        }, {
            "object": "dot",
            "activity": "drawing",
            "goal": "taking turns",
            "activity_result": "group of dots"
        }, {
            "object": "animals",
            "activity": "naming",
            "goal": "taking turns",
            "activity_result": "animals"
        }
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


b_activity = BuildActivityComponent()
b_activity.print_components()

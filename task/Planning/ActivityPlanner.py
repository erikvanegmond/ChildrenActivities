from activity.Activity import Activity
from task.Planning.Requirements import Requirements


class Planner:
    def __init__(self):
        self.requirements = Requirements()
        self.num_plans_per_batch = 10

    def run(self):
        activities = []
        for i in range(self.num_plans_per_batch):
            activities.append(self.generate_plans())
            activities = self.filter(activities, self.requirements.hard_requirements())
            activities = self.sort(activities, self.requirements.soft_requirements())

        print(activities)

    @staticmethod
    def filter(activities, hard_requirements):
        # TODO: implement filter
        return activities

    @staticmethod
    def sort_activities(activities, soft_requirements):
        # TODO: implement sort
        return activities

    def operationalize(self):
        # TODO: implement operationalize
        pass

    def generate_plans(self):
        # TODO: implement plan generator
        while True:
            yield Activity()

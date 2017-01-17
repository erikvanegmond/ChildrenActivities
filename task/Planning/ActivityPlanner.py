from activity.Activity import Activity
from task.Planning.Requirements import Requirements


class Planner:
    def __init__(self):
        self.requirements = Requirements()
        self.goal = None
        self.num_plans_per_batch = 10
        self.run()

    def run(self):
        activities = []
        for i in range(self.num_plans_per_batch):
            activities.append(self.generate_plans(self.goal))
        activities = self.select_subset(activities, self.requirements.hard_requirements())
        activities = self.sort_activities(activities, self.requirements.soft_requirements())

        print(activities)

    @staticmethod
    def select_subset(activities, hard_requirements):
        # TODO: implement filter
        return activities

    @staticmethod
    def sort_activities(activities, soft_requirements):
        # TODO: implement sort
        return activities

    def operationalize(self):
        # TODO: implement operationalize
        pass

    def generate_plans(self, goal):
        # TODO: implement plan generator
        while True:
            yield Activity(goal)

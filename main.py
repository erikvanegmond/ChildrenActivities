import argparse

from child.examples import example_child
from task.Assessment.Assessment import Assessment
from task.Configuration.Activity import ActivityConfiguration


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--example', action='store_true')
    parser.add_argument('-child', choices=["Bob", "Lisa"])
    args = parser.parse_args()

    if args.example:
        if args.child:
            example = example_child(args.child)
        else:
            example = None
            while example is None:
                child = input("What example child do you want?")
                example = example_child(child)

        assessment = Assessment(child=example)
    else:
        assessment = Assessment()
    assessment.assess_child()
    focus = assessment.decide_focus_norm()
    print(assessment.child)
    print("{} needs to focus on {}".format(assessment.child.name, focus[1]))
    act = ActivityConfiguration(goal=focus[1], assessed_age=focus[0])
    act.run()


if __name__ == '__main__':
    run()

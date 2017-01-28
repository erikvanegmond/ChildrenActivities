from task.Assessment.Assessment import Assessment
from child.examples import example_child
import argparse


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--example', action='store_true')
    args = parser.parse_args()

    if args.example:
        print('example time!')

        example = None
        while example is None:
            child = input("What example child do you want?")
            example = example_child(child)

        assessment = Assessment(child=example)
    else:
        print("just do it yourself!")
        assessment = Assessment()
    print(assessment.child)
    assessment.assess_child()
    assessment.decide_focus_norm()


if __name__ == '__main__':
    run()

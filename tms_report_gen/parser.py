import csv

from tms_report_gen.models import TestCase, TestStep


def str_to_bool(value: str) -> bool:
    return value.lower() == "true"

def parse_int(value: str) -> int | None:

    try:
        return int(value)

    except (ValueError, TypeError):
        return None


def load_test_cases(
    cases_csv_path: str,
    steps_csv_path: str,
) -> list[TestCase]:

    test_cases = {}

    # Loading test cases from cases CSV file
    with open(cases_csv_path, newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            testcase = TestCase(
                id=int(row["id"]),

                name=row["name"],
                title=row["title"],

                status=parse_int(row["status"]),

                is_tracked=str_to_bool(row["is_tracked"]),
                is_auto=str_to_bool(row["is_auto"]),
                is_individ=str_to_bool(row["is_individ"]),
                is_unique=str_to_bool(row["is_unique"]),

                priority=parse_int(row["priority"]),
                test_type=parse_int(row["type"]),
                complexity=parse_int(row["complexity"]),

                steps=[]
            )

            test_cases[testcase.id] = testcase

    # Loading test steps from steps CSV file
    with open(steps_csv_path, newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            step = TestStep(
                id=int(row["id"]),
                step_type=row["step_type"],
                action=row["action"],
                expected_result=row["expected_result"],
                order=parse_int(row["order"]),
            )

            case_id = int(row["case_id"])

            if case_id in test_cases:
                test_cases[case_id].steps.append(step)

    # Sorting steps for each case
    for testcase in test_cases.values():
        testcase.steps.sort(key=lambda step: step.order)

    return list(test_cases.values())
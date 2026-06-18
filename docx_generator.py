from models import TestCase


def generate_docx(
    testcase: TestCase,
    output_path: str,
):

    print(f"[DOCX] {testcase.name} -> {output_path}")
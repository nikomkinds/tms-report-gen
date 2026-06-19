from pathlib import Path

from weasyprint import HTML

from tms_report_gen.models import TestCase

TEMPLATES_DIR = (
    Path(__file__).parent / "templates"
)


# Generating PDF report for test case
def generate_pdf(
    testcase: TestCase,
    output_path: str,
):

    html = build_html(testcase)

    HTML(string=html).write_pdf(output_path)

# Building HTML content for test case report using template and test case data
def build_html(testcase: TestCase) -> str:

    template_path = TEMPLATES_DIR / "testcase.html"

    template = template_path.read_text(encoding="utf-8")

    steps_html = build_steps_html(testcase)

    html = (
        template
        .replace("{{ID}}", str(testcase.id))
        .replace("{{NAME}}", testcase.name)
        .replace("{{TITLE}}", testcase.title)
        .replace("{{STATUS}}", str(testcase.status))
        .replace("{{IS_TRACKED}}", str(testcase.is_tracked))
        .replace("{{IS_AUTO}}", str(testcase.is_auto))
        .replace("{{IS_INDIVID}}", str(testcase.is_individ))
        .replace("{{IS_UNIQUE}}", str(testcase.is_unique))
        .replace("{{PRIORITY}}", str(testcase.priority))
        .replace("{{TYPE}}", str(testcase.test_type))
        .replace("{{COMPLEXITY}}", str(testcase.complexity))
        .replace("{{STEPS}}", steps_html)
    )

    return html

# Building HTML content for test case steps
def build_steps_html(testcase: TestCase) -> str:

    result = ""

    for step in testcase.steps:

        expected_result = ""

        if step.expected_result:
            expected_result = f"""
            <div>
                <b>Expected result:</b>
                {step.expected_result}
            </div>
            """

        step_html = f"""
        <div class="step">

            <div class="step-title">
                Step #{step.order} ({step.step_type})
            </div>

            <div>
                {step.action}
            </div>

            {expected_result}

        </div>
        """

        result += step_html

    return result
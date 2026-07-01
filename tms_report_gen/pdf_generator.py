from pathlib import Path

from jinja2 import Environment
from jinja2 import FileSystemLoader

from weasyprint import HTML

from tms_report_gen.models import TestCase
from tms_report_gen.utils import resolve_image_paths


TEMPLATES_DIR = (
    Path(__file__).parent / "templates"
)

env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=True,
)


# Generating PDF report for test case
def generate_pdf(
    testcase: TestCase,
    output_path: str,
    media_root: str,
):

    html = build_html(testcase, media_root)

    HTML(string=html).write_pdf(output_path)


# Building HTML content for test case report using Jinja2 template
def build_html(
    testcase: TestCase,
    media_root: str,
) -> str:

    template = env.get_template(
        "testcase.html"
    )

    for step in testcase.steps:

        step.action = resolve_image_paths(
            step.action,
            media_root,
        )

        if step.expected_result:

            step.expected_result = (
                resolve_image_paths(
                    step.expected_result,
                    media_root,
                )
            )

    html = template.render(
        testcase=testcase
    )

    return html
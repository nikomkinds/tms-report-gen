from pathlib import Path

from jinja2 import Environment
from jinja2 import FileSystemLoader

from weasyprint import HTML

from tms_report_gen.models import TestCase


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
):

    html = build_html(testcase)

    HTML(string=html).write_pdf(output_path)


# Building HTML content for test case report using Jinja2 template
def build_html(testcase: TestCase) -> str:

    template = env.get_template(
        "testcase.html"
    )

    html = template.render(
        testcase=testcase
    )

    return html
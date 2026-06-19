from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Pt

from tms_report_gen.models import TestCase


def generate_docx(
    testcase: TestCase,
    output_path: str,
):

    doc = Document()

    # Heading - test case name
    doc.add_heading(testcase.name, level=1)

    # Test case attributes list
    doc.add_heading("Информация о тест-кейсе", level=2)

    add_attribute(doc, "ID", testcase.id)
    add_attribute(doc, "Title", testcase.title)
    add_attribute(doc, "Status", testcase.status)

    add_attribute(doc, "Tracked", testcase.is_tracked)
    add_attribute(doc, "Auto", testcase.is_auto)
    add_attribute(doc, "Individual", testcase.is_individ)
    add_attribute(doc, "Unique", testcase.is_unique)

    add_attribute(doc, "Priority", testcase.priority)
    add_attribute(doc, "Type", testcase.test_type)
    add_attribute(doc, "Complexity", testcase.complexity)

    # Steps section
    doc.add_heading("Шаги", level=2)

    for step in testcase.steps:

        title = (
            f"Step #{step.order} "
            f"({step.step_type})"
        )

        doc.add_heading(title, level=3)

        parse_html(doc, step.action)

        if step.expected_result:

            p = doc.add_paragraph()

            run = p.add_run("Expected result:")
            run.bold = True

            parse_html(doc, step.expected_result)


    doc.save(output_path)


def add_attribute(
    doc: Document,
    name: str,
    value,
):

    p = doc.add_paragraph()

    key_run = p.add_run(f"{name}: ")
    key_run.bold = True

    p.add_run(str(value))


def parse_html(
    doc: Document,
    html: str,
):

    soup = BeautifulSoup(html, "html.parser")

    # Top-level elements handling
    for element in soup.contents:

        # Paragraphs
        if element.name == "p":

            p = doc.add_paragraph()

            # <b>, <i>, <code> and <br> tags handling (inside this paragraph)
            parse_inline_tags(p, element)

        
        # Code blocks
        elif element.name == "pre":

            code_text = element.get_text()

            p = doc.add_paragraph()

            run = p.add_run(code_text)

            run.font.name = "Courier New"
            run.font.size = Pt(10)

        
        # Unhandled tags
        elif isinstance(element, str):

            text = element.strip()

            if text:
                doc.add_paragraph(text)


def parse_inline_tags(
    paragraph,
    parent,
):

    for child in parent.children:

        # Simple text
        if isinstance(child, str):

            paragraph.add_run(child)

        # Bold
        elif child.name == "b":

            run = paragraph.add_run(
                child.get_text()
            )

            run.bold = True

        # Italic
        elif child.name == "i":

            run = paragraph.add_run(
                child.get_text()
            )

            run.italic = True

        # Code
        elif child.name == "code":

            run = paragraph.add_run(
                child.get_text()
            )

            run.font.name = "Courier New"

        # Line break
        elif child.name == "br":

            paragraph.add_run("\n")

        # Unhandled tag
        else:

            paragraph.add_run(
                child.get_text()
            )
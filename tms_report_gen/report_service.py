from pathlib import Path

from tms_report_gen.parser import load_test_cases
from tms_report_gen.utils import sanitize_filename

from tms_report_gen.pdf_generator import generate_pdf
from tms_report_gen.docx_generator import generate_docx

# Generate all reports for the given test cases with the specified format and save them to the output directory
def generate_reports(
        cases_csv_path: str,
        steps_csv_path: str,
        output_dir: str,
        media_root: str,
        report_format: str | None = None,
):
    # Load test cases from CSV files
    test_cases = load_test_cases(cases_csv_path, steps_csv_path)

    # Create the output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for test_case in test_cases:

        # Creating a safe filename
        safe_name = sanitize_filename(test_case.name)
        base_filename = f"{test_case.id}_{safe_name}"

        # PDF
        if report_format in ["pdf", None]:

            pdf_path = output_path / f"{base_filename}.pdf"
            generate_pdf(
                test_case, 
                str(pdf_path), 
                media_root,
            )

            print(f"[PDF] Created: {pdf_path}")
        
        # DOCX
        if report_format in ["docx", None]:

            docx_path = output_path / f"{base_filename}.docx"
            generate_docx(
                test_case, 
                str(docx_path),
                media_root
            )

            print(f"[DOCX] Created: {docx_path}")
        
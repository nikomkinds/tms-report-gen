from tms_report_gen import generate_reports


generate_reports(
    cases_csv_path="case_case.csv",         # Cases CSV file path
    steps_csv_path="case_casestep.csv",     # Case steps CSV file path
    output_dir="reports",                   # Output directory path
    report_format="pdf",                    # Report format: "pdf", "docx" or None for both
    media_root="C:/root/exports",           # Media root directory path
)
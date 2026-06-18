from report_service import generate_all_reports


generate_all_reports(
    cases_csv_path="case_case.csv",
    steps_csv_path="case_casestep.csv",
    output_dir="reports",
)
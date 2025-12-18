def format_linter_error(error: dict) -> dict:
   
   return {
       "line" : error["line_number"],
        "column" : error["column_number"],
        "message" : error["text"],
        "name": error["code"],
        "source": error["filename"]
        }

def format_single_linter_file(file_path: str, errors: list) -> dict:

    return { "errors" : [
                format_linter_error(error)
            for item in errors],
            "path": 'flake8', 
            "status": "failed" if item else 'passed'
        }


def format_linter_report(linter_report: dict) -> list:

    return [
        format_single_linter_file(file_path, errors)
        for path, values in linter_report.items()
    ]
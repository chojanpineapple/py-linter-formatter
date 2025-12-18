def format_linter_error(error: dict) -> dict:
   
   return {
       "line" : error["line_number"],
        "column" : error["column_number"],
        "message" : error["text"],
        "name": error["code"],
        "source": error["filename"]
        }

def format_single_linter_file(file_path: str, errors: list) -> dict:

    return { "error" : [
                {
                "line" : item["line_number"],
                "column" : item["column_number"], 
                "message" : item["text"], 
                "name": item["code"], 
                "source": item["filename"] }
            for item in errors],
            "path": file_path, 
            "status": "failed"
        }


def format_linter_report(linter_report: dict) -> list:
    
    return [
        {
            "errors": [
                {
                    "line": item["line_number"],
                    "column": item["column_number"],
                    "message": item["text"],
                    "name": item["code"],
                    "source": item["filename"],
                }
                for item in values
            ],
            "path": path,
            "status": "failed" if values else "passed",
        }
        for path, values in linter_report.items()
    ]
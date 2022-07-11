def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            format_linter_error(error)
            for error in errors
        ],
        "path": file_path,
        "status": "passed" if errors == [] else "failed",
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, linter_report[file_path])
        for file_path in linter_report
    ]
    pass

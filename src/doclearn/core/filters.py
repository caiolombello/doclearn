from datetime import datetime


def filter_markdown_files(
    md_files,
    name_query=None,
    min_size=None,
    max_size=None,
    min_date=None,
    max_date=None,
    path_query=None,
):
    filtered_files = []

    for file in md_files:
        if name_query and name_query.lower() not in file["name"].lower():
            continue
        if min_size and file["size"] < min_size:
            continue
        if max_size and file["size"] > max_size:
            continue
        if min_date or max_date:
            file_date = datetime.strptime(file["last_modified"], "%Y-%m-%dT%H:%M:%SZ")
            if min_date and file_date < min_date:
                continue
            if max_date and file_date > max_date:
                continue
        if path_query and path_query.lower() not in file["path"].lower():
            continue

        filtered_files.append(file)

    return filtered_files

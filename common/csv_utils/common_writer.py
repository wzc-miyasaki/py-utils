import csv
import os

def listMap_to_csv(data: list[dict], filename: str, mode="w"):
    """
    Writes a list of dictionaries to a CSV file.

    :param data: List of dictionaries to write.
    :param filename: Name of the output CSV file.
    :param mode: File mode - 'w' for overwrite, 'a' for append. Default is 'w'.
    """
    if not data:
        raise ValueError("The data list is empty. Cannot write to CSV.")

    # Ensure all rows have the same keys (find all unique keys)
    fieldnames = set()
    for row in data:
        fieldnames.update(row.keys())

    fieldnames = sorted(fieldnames)  # Sort keys for consistent column order

    # Write to CSV
    file_exists = os.path.exists(filename)

    with open(filename, mode, newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header only if creating a new file
        if mode == "w" or not file_exists:
            writer.writeheader()

        for row in data:
            writer.writerow(row)

    print(f"CSV file '{filename}' written successfully!")


def dict_to_csv(data: dict, filename: str, titlenames: str, mode="w"):
    """
    Writes a list of dictionaries to a CSV file.

    :param data: List of dictionaries to write.
    :param filename: Name of the output CSV file.
    :param mode: File mode - 'w' for overwrite, 'a' for append. Default is 'w'.
    """
    if not data:
        raise ValueError("The data list is empty. Cannot write to CSV.")

    # Write to CSV
    file_exists = os.path.exists(filename)

    with open(filename, mode, newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=titlenames)

        # Write header only if creating a new file
        if mode == "w" or not file_exists:
            writer.writeheader()

        for item in data.items():
            row = dict(item)
            writer.writerow(row)

    print(f"CSV file '{filename}' written successfully!")
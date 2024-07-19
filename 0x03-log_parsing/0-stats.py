#!/usr/bin/python3
import sys
import re
from collections import defaultdict


def update_metrics(line):
    """
    Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    """
    match = re.match(
        r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)',
        line)
    if match:
        ip_address, date, status_code, file_size = match.groups()
        status_code = int(status_code)
        file_size = int(file_size)
        return file_size
    else:
        return 0


try:
    line_count = 0
    total_file_size = 0
    status_codes = defaultdict(int)

    while True:
        try:
            line = input()
        except KeyboardInterrupt:
            break

        new_file_size = update_metrics(line)
        if new_file_size > 0:
            total_file_size += new_file_size
            status_code = int(match.group(3))
            status_codes[status_code] += 1
            line_count += 1

        if line_count % 10 == 0:
            print(f"Total file size: {total_file_size}")
            print("Number of lines by status code:")
            for code in sorted(status_codes):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
            print()

    print(f"Total file size: {total_file_size}")
    print("Number of lines by status code:")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    print("\nStatistics:")
    print(f"Total file size: {total_file_size}")
    print("Number of lines by status code:")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


if __name__ == '__main__':
    run()

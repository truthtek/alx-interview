#!/usr/bin/python3
"""
Read stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
After every 10 lines or keyboard interrupt (CTRL + C):
Print statistics from the beginning
"""
import sys
import re


def print_stats(total_size, status_codes):
    """Print accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """Parse a line and return the status code and file size"""
    pattern = r'^(\S+) - \[(.+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    match = re.match(pattern, line)
    if match:
        return match.group(3), int(match.group(4))
    return None, None


total_size = 0
line_count = 0
status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}

try:
    for line in sys.stdin:
        line = line.strip()
        status, file_size = parse_line(line)
        
        if status and file_size is not None:
            total_size += file_size
            if status in status_codes:
                status_codes[status] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

except KeyboardInterrupt:
    pass
finally:
    print_stats(total_size, status_codes)

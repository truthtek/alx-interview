#!/usr/bin/python3
"""
Read stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_codes):
    """Print accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


total_size = 0
line_count = 0
status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        
        try:
            size = int(data[-1])
            total_size += size
        except (IndexError, ValueError):
            pass

        try:
            status = data[-2]
            if status in status_codes:
                status_codes[status] += 1
        except IndexError:
            pass

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    pass
finally:
    print_stats(total_size, status_codes)

#!/usr/bin/python3
import sys
import re

def print_msg(status_code_counts, total_size):
    print("File size: {}".format(total_size))
    for key, val in sorted(status_code_counts.items()):
        if val != 0:
            print("{}: {}".format(key, val))

status_code_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        parsed_line = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
        if parsed_line:
            counter += 1
            total_size += int(parsed_line.group(4))
            code = parsed_line.group(3)
            if code in status_code_counts:
                status_code_counts[code] += 1
        if counter == 10:
            print_msg(status_code_counts, total_size)
            counter = 0
    print_msg(status_code_counts, total_size)
except Exception as e:
    print("Error: {}".format(e))

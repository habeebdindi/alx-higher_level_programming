#!/usr/bin/python3
"""
compute metrics
"""
import sys


codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
count = 0
sum_size = 0
status_counts = {code: 0 for code in codes}

try:
    for line in sys.stdin:
        count += 1
        line = line.strip()
        words = line.split()
        sum_size += int(words[8])

        status_code = words[7]
        if status_code in codes:
            status_counts[status_code] += 1

        if count % 10 == 0:
            print("File size: {}".format(sum_size))
            for code in sorted(status_counts):
                if status_counts[code] != 0:
                    print("{}: {}".format(code, status_counts[code]))

except KeyboardInterrupt as e:
    print("File size: {}".format(sum_size))
    for code in sorted(status_counts):
        if status_counts[code] != 0:
            print("{}: {}".format(code, status_counts[code]))
    print(e)

#!/usr/bin/python3
"""Log Parsing"""
import sys


codes = [200, 301, 400, 401, 403, 404, 405, 500]
count = {k: 0 for k in codes}
loops = total = 0


def print_codes(codes, file_size):
    ''' Print all status codes generated so far '''
    print("File size: {}".format(total))
    for code in sorted(count):
        if count[code] != 0:
            print("{}: {}".format(code, count[code]))


try:
    for line in sys.stdin:
        loops += 1

        split = line.split()
        if len(split) != 9:
            continue
        if len(split[0].split(".")) != 4:
            continue

        status = int(split[7])
        if status in codes:
            count[status] += 1

        total += int(split[8])

        if loops == 10:
            loops = 0
            print_codes(count, total)
except (KeyboardInterrupt, TypeError) as e:
    print_codes(count, total)
    print(e)

print_codes(count, total)

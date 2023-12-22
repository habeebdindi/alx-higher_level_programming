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
        split = line.strip().split()

        try:
            status = int(split[-2])
            if status in codes:
                count[status] += 1
        except Exception:
            pass

        try:
            total += int(split[-1])
        except Exception:
            pass

        if loops == 10:
            loops = 0
            print_codes(count, total)
except (KeyboardInterrupt, ValueError) as e:
    print_codes(count, total)
    raise

print_codes(count, total)

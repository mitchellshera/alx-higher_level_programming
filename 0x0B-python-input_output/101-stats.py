#!/usr/bin/python3

import sys


def print_statistics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    parts = line.split()
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = int(parts[-1])
    return ip_address, status_code, file_size

def main():
    count = 0
    total_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line.strip())
            count += 1
            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            if count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()

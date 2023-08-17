#!/usr/bin/python3
import sys
import signal

def print_statistics(status_codes, total_size):
    """Prints the statistics"""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """Handles the CTRL+C interruption"""
    print_statistics(status_codes, total_size)
    sys.exit(0)

# Initial metrics
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_size = 0
line_count = 0

# Setting up the CTRL+C signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        tokens = line.split()
        try:
            # Extracting IP, status_code and file_size from log line
            size = int(tokens[-1])
            status = int(tokens[-2])
            
            if status in status_codes:
                status_codes[status] += 1

            total_size += size
            line_count += 1

            # Printing after 10 lines
            if line_count % 10 == 0:
                print_statistics(status_codes, total_size)

        except:
            # Ignoring lines that do not match the expected format
            pass
finally:
    # Printing at the end
    print_statistics(status_codes, total_size)

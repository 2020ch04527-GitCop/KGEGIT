import csv
import re
import pandas as pd
from collections import Counter
import os

"""
# Purpose:
# This script analyzes a web server access log to count the number of requests made by each IP address,
# parses the log into a DataFrame, and saves the results to CSV and HTML files.
#
# Steps performed:
1. Reads an access log file line by line.
2. Extracts the IP address and other fields from each log entry and parses them into a list of dictionaries.
3. Counts the number of requests per IP address using collections.Counter.
4. Converts the parsed log data to a pandas DataFrame.
5. Saves only the first 20 parsed log lines to a CSV file (overwriting it each time).
6. Saves the entire parsed log as a colored HTML table with a colored header and table outline.
7. Identifies the top 5 IP addresses by request count (printed to console, not saved to CSV).
"""

# Get the directory of the current Python file
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_dir, 'access.log')
csv_file_path = os.path.join(script_dir, 'parsed_log.csv')
html_file_path = os.path.join(script_dir, 'parsed_log.html')

log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>\w+) (?P<endpoint>[^ ]+) [^"]+" (?P<status>\d+) (?P<size>\d+)')

def parse_log(file_path):
    """Generator that yields a dictionary for each valid log line."""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                yield match.groupdict()

# Use generator to avoid storing all lines in memory
records_gen = parse_log(log_file_path)
records = list(records_gen)

# Use Counter with a generator expression for IPs
ip_counter = Counter(rec['ip'] for rec in records)
print('Requests per IP:')
for ip, count in ip_counter.items():
    print(f'{ip}: {count}')

# Convert to DataFrame and save results
if records:
    df = pd.DataFrame(records)
    print('\nDataFrame preview:')
    print(df.head())
    # Save only the first 20 lines to CSV (overwrite, do not append)
    df.head(20).to_csv(csv_file_path, index=False)
    # Save to HTML with colored header and table outline (all records)
    html = df.to_html(index=False, border=2, classes='log-table')
    style = '''<style>
    .log-table { border-collapse: collapse; width: 100%; }
    .log-table th { background-color: #4CAF50; color: white; border: 2px solid #333; }
    .log-table td { border: 2px solid #333; }
    </style>'''
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(style + html)
    print(f"\nSaved first 20 parsed log lines to '{csv_file_path}' and all to '{html_file_path}' with colored header and table outline.")
    # Identify top 5 IPs by request count (printed only)
    top_5 = ip_counter.most_common(5)
    print('\nTop 5 IP addresses by request count:')
    for ip, count in top_5:
        print(f'{ip}: {count}')
else:
    print('No valid log entries found.')
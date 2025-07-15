import csv
import math
from collections import defaultdict, Counter

FILENAME = 'SocialMediaTop100.csv'

# Helper functions
def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def stddev(nums, mean):
    if len(nums) < 2:
        return 0.0
    return math.sqrt(sum((x - mean) ** 2 for x in nums) / (len(nums) - 1))

def analyze(rows, columns):
    stats = {}
    for col in columns:
        values = [row[col] for row in rows if row[col] != '']
        if all(is_float(v) for v in values):
            nums = [float(v) for v in values]
            count = len(nums)
            mean = sum(nums) / count if count else 0
            minv = min(nums) if nums else None
            maxv = max(nums) if nums else None
            std = stddev(nums, mean) if count > 1 else 0
            stats[col] = {
                'count': count,
                'mean': mean,
                'min': minv,
                'max': maxv,
                'std': std
            }
        else:
            count = len(values)
            unique = set(values)
            freq = Counter(values)
            most_common = freq.most_common(1)[0] if freq else (None, 0)
            stats[col] = {
                'count': count,
                'unique_count': len(unique),
                'most_frequent': most_common
            }
    return stats

def print_stats(title, stats):
    print(f'\n--- {title} ---')
    for col, stat in stats.items():
        print(f'{col}: {stat}')

def groupby(rows, group_cols):
    groups = defaultdict(list)
    for row in rows:
        key = tuple(row[col] for col in group_cols)
        groups[key].append(row)
    return groups

def main():
    with open(FILENAME, newline='', encoding='ISO-8859-1') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    columns = reader.fieldnames

    # Overall stats
    stats = analyze(data, columns)
    print_stats('Overall', stats)

    # By Platform
    for platform, rows in groupby(data, ['Platform']).items():
        stats = analyze(rows, columns)
        print_stats(f'Platform={platform[0]}', stats)

    # By Platform + PROFILE
    for key, rows in groupby(data, ['Platform', 'PROFILE']).items():
        stats = analyze(rows, columns)
        print_stats(f'Platform={key[0]}, PROFILE={key[1]}', stats)

if __name__ == '__main__':
    main() 
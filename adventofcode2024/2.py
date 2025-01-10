with open('2.txt', 'r') as f:
    lines = f.read().split('\n')

reports = []
for line in lines:
    reports.append(list(map(int, line.split())))

def check_line(line):
    prev_diff = 0
    cur = line[0]
    for nxt in line[1:]:
        diff = nxt-cur
        if not 1 <= abs(nxt-cur) <= 3:
            return False
        if prev_diff*diff < 0:
            return False
        prev_diff = diff
        cur = nxt
    return True

answer1 = sum(1 for report in reports if check_line(report))
print(answer1)

answer2 = 0
for report in reports:
    for i in range(len(report)):
        tmp = report[:i] + report[i+1:]
        if check_line(tmp):
            answer2 += 1
            break
print(answer2)

### ChatGPT-4o answer => mind-blowing🤯
def is_safe(report):
    """
    Check if a report is safe.
    """
    increasing = all(1 <= b - a <= 3 for a, b in zip(report, report[1:]))
    decreasing = all(1 <= a - b <= 3 for a, b in zip(report, report[1:]))
    return increasing or decreasing


def is_safe_with_dampener(report):
    """
    Check if a report is safe, considering the Problem Dampener.
    """
    if is_safe(report):
        return True
    
    # Check by removing each level
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    
    return False


def analyze_reports(reports, part_two=False):
    """
    Analyze all reports and count safe ones.
    """
    safe_count = 0
    for report in reports:
        if part_two:
            if is_safe_with_dampener(report):
                safe_count += 1
        else:
            if is_safe(report):
                safe_count += 1
    return safe_count


# Example Input
example_data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

# Part One
print("Safe reports (Part 1):", analyze_reports(example_data))

# Part Two
print("Safe reports (Part 2):", analyze_reports(example_data, part_two=True))
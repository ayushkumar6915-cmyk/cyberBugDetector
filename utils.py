def save_report(report, path):
    with open(path, 'w') as f:
        for line in report:
            f.write(line + "\n")
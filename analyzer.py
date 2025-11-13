def analyze_file(file_path):
    bugs = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines, start=1):
            if "password" in line:
                bugs.append(f"Line {i}: Hardcoded password detected")
            if "eval(" in line:
                bugs.append(f"Line {i}: Use of eval() is dangerous")
            if "pickle.loads" in line:
                bugs.append(f"Line {i}: Insecure deserialization with pickle")
            if "SELECT *" in line and "WHERE" in line:
                bugs.append(f"Line {i}: Possible SQL Injection")
    return bugs
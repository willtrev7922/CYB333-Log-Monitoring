print("CYB333 Security Log Monitoring System")
print("-------------------------------------")

with open("sample_logs.txt", "r", encoding="utf-8") as log_file:
    for line in log_file:
        print(line.strip())
from pathlib import Path

# print("Working directory:", Path.cwd())
# print("Script directory:", Path(__file__).resolve().parent)

log_path = Path(__file__).resolve().parent / "logs.txt"
d = {}
runs = []
with open(log_path, "r") as file:
    for line in file:
        parts = line.split()
        if len(parts) >= 2:
            runs.append(line.split(" "))


# print(runs)
keys = []
values = []
for i in range(len(runs)):
    keys.append(runs[i][0])
    values.append(runs[i][1])

# print(keys, values)

unique_keys = []
for key in keys:
    if key not in unique_keys:
        unique_keys.append(key)

# print(unique_keys)

for key in unique_keys:
    run_ids = []
    for i in range(len(keys)):
        if keys[i] == key:
            run_ids.append(values[i])
    d[key] = run_ids

# print(d)
for k in d:
    print(f"{k}: {len(d[k])}")

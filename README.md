# Training Log Analyzer

A small Python command-line program that reads training run logs, groups run IDs by status, and prints the number of runs for each status.

## Run locally

Use Python 3 and keep `logs.txt` next to `main.py`. Run this command from the project folder.

```sh
python main.py
```

## Example

Each line in `logs.txt` starts with a status followed by a run ID. The script skips blank lines and entries without a run ID.

```text
OK run-01
FAILED run-02
OK run-03
```

The script prints the following totals.

```text
OK: 2
FAILED: 1
```


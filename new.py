import os
import re
import sys
from datetime import datetime

WEEK_DIR = "weeks"
PROOF_DIR = "proofs"



def get_last_week_number() -> int:
    files = os.listdir(WEEK_DIR)

    numbers = [1] + [
        int(re.search(r"(\d+)\.yaml$", file).group(1))
        for file in files
        if re.match(r"\d+\.yaml$", file)
    ]

    return max(numbers)


def get_new_week_filename():
    return f"{get_last_week_number()+1:02}.yaml"


def append_pid_to_week(pid):
    filename = f"{WEEK_DIR}/{get_last_week_number():02}.yaml"
    with open(filename, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("proofs:"):
            if "[]" in line:
                lines[i] = f"proofs:\n  - {pid}\n"
            else:
                for j in range(i + 1, len(lines)):
                    if not lines[j].startswith("  - "):
                        lines.insert(j, f"  - {pid}\n")
                        break
                else:
                    lines.append(f"  - {pid}\n")
            break

    with open(filename, "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    selected = input("What do you want to create (week, proof) :")

    if selected == "week":
        while (date := input("Monday’s date (eg. 07/04/2025): ").strip()) == "":
            print("Invalid input. Try again.")

        description = input("Description: ")

        content = f"""date: {date}
description: "{description}"
proofs: []
        """

        with open(f"{WEEK_DIR}/{get_new_week_filename()}", "w") as f:
            f.write(content)
    else:
        while (title := input("Title: ").strip()) == "":
            print("Invalid input. Try again.")

        # while (authors := input("Authors (comma separated): ").strip()) == '':
        #     print("Invalid input. Try again.")
        authors = input("Authors (comma separated) [default: ADD A DEFAULT]: ").strip()
        if len(authors) == 0:
            authors = "ADD A DEFAULT"

        authors = authors.split(",") if len(authors) > 0 else None
        if authors is not None:
            authors = "\n  - " + "\n  - ".join([t for t in authors])

        date = datetime.now().strftime("%d/%m/%Y")

        pid = int(datetime.now().timestamp())

        tags = input("Tags (comma separated): ").strip()
        tags = tags.split(",") if len(tags) > 0 else None
        if tags is not None:
            tags = "\n  - " + "\n  - ".join([t for t in tags])

        content = f"""---
title: {title}
authors:{authors or " []"}
date: {date}
pid: {pid}
tags:{tags or " []"}
---

question

---

proof"""
        with open(f"{PROOF_DIR}/{pid}.md", "w") as f:
            f.write(content)

        append_pid_to_week(pid)

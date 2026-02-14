import os

def generate_readme():
    base_dir = "problems"
    problems = []

    # Scan the problems directory
    if not os.path.exists(base_dir):
        return

    for folder in sorted(os.listdir(base_dir)):
        # Expecting format: 0001-two-sum
        parts = folder.split('-', 1)
        if len(parts) == 2:
            num, name = parts
            title = name.replace('-', ' ').title()
            link = f"./{base_dir}/{folder}/"
            problems.append(f"| {num} | [{title}]({link}) | [Link](https://leetcode.com/problems/{name}/) |")

    # Readme Template
    header = "# LeetCode Solutions\n\nMy personal archive of LeetCode challenges.\n\n"
    table_header = "| # | Problem | LeetCode Link |\n|---|---|---|\n"
    
    with open("README.md", "w") as f:
        f.write(header + table_header + "\n".join(problems))

if __name__ == "__main__":
    generate_readme()
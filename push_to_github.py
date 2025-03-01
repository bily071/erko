import subprocess

# Correct repository path
repo_path = r"C:\Users\User\Desktop\python\IT Academy\ermin_bilal_python\Test Automation and Quality Assurance\repo"

# List of Git commands
commands = [
    ["git", "-C", repo_path, "pull", "origin", "main", "--allow-unrelated-histories"],
    ["git", "-C", repo_path, "add", "."],
    ["git", "-C", repo_path, "commit", "-m", "Added Python files"],
    ["git", "-C", repo_path, "push", "origin", "main"]
]

# Execute each command
for command in commands:
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        break  # Stop execution if any command fails

print("✅ Files successfully pushed to GitHub!")


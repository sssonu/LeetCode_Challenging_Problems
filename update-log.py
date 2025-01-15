from datetime import datetime
import os

# File to update
file_path = "requirements.txt"

# Number of commits to make
commits_per_day = 10

# Get the current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create or append to the log file
if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write("Daily Log:\n")

# Add multiple log entries for multiple commits
for i in range(1, commits_per_day + 1):
    with open(file_path, "a") as file:
        file.write(f"{current_time} - Commit {i}\n")
    # Stage the change and commit
    os.system(f"git add {file_path}")
    os.system(f"git commit -m 'Automated commit {i} at {current_time}'")

print(f"Generated {commits_per_day} commits for {current_time}.")

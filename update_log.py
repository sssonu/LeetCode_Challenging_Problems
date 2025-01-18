from datetime import datetime
import os
import subprocess

# File to update
file_path = "daily_log.txt"

# Number of commits to make
commits_per_day = 10

# Get the current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create the log file if it doesn't exist
if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write("Daily Log:\n")

# Add multiple log entries for multiple commits
for i in range(1, commits_per_day + 1):
    with open(file_path, "a") as file:
        file.write(f"{current_time} - Commit {i}\n")
    
    try:
        # Stage the changes
        subprocess.run(["git", "add", file_path], check=True)
        # Commit the changes
        subprocess.run(
            ["git", "commit", "-m", f"Automated commit {i} at {current_time}"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error during commit {i}: {e}")
        break

print(f"Generated {commits_per_day} commits for {current_time}.")

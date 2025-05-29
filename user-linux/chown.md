# chown Commands for User 'student1' and Group 'developers'
# Example path: /home/student1/project1/

# Permission Explanation:
# - User 'student1' can change ownership of files and directories they own.
# - Changing ownership to user 'student1' and group 'developers' requires sudo/root privileges.
# - Typically, you need to run these commands with sudo if you are not root.
# - Use 'sudo' if necessary, e.g. sudo chown ...

# Change ownership of a single file to user 'student1' and group 'developers'
chown student1:developers /home/student1/project1/file.txt

# Change ownership of a single directory to user 'student1' and group 'developers'
chown student1:developers /home/student1/project1/

# Change ownership recursively for all files and directories inside project1
chown -R student1:developers /home/student1/project1/

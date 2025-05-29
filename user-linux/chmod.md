# All Symbolic chmod Combinations Including u+x
# Example path: /home/student1/project1/

# Permission Explanation:
# - User 'student1' can run these chmod commands on files and directories they own.
# - Typically, 'student1' owns everything inside /home/student1/, so no sudo or root is needed.
# - If 'student1' tries to change permissions on files owned by others, sudo/root is required.
# - Use 'sudo' only if you need to modify files not owned by your user.

# Note: These commands apply to files or directories at this path.
#       Use the -R option to apply changes recursively inside the directory.

chmod u+x /home/student1/project1/file.txt            # Add execute permission for user on a file
chmod u+xw /home/student1/project1/file.txt           # Add execute and write permissions for user on a file
chmod u+xr /home/student1/project1/file.txt           # Add execute and read permissions for user on a file
chmod u+rwx /home/student1/project1/file.txt          # Add read, write, execute permissions for user on a file

chmod ug+x /home/student1/project1/script.sh           # Add execute for user and group on a file
chmod uo+x /home/student1/project1/script.sh           # Add execute for user and others on a file
chmod ugo+x /home/student1/project1/script.sh          # Add execute for user, group, and others on a file
chmod ug+x,o+r /home/student1/project1/data.txt        # Add execute for user & group, add read for others on a file
chmod u+x,g-w /home/student1/project1/data.txt          # Add execute for user, remove write from group on a file

chmod u+x,g=r /home/student1/project1/                  # Add execute for user, set group to read only on the directory
chmod u+x,o-r /home/student1/project1/                  # Add execute for user, remove read from others on the directory
chmod u+x,g+x,o+x /home/student1/project1/              # Explicitly add execute for user, group, others on the directory

# To apply changes recursively inside the project directory:
chmod -R u+x /home/student1/project1/

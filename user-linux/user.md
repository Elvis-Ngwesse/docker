------------------------------------------------------------
✅ 1. Create a New User
------------------------------------------------------------

Debian:
sudo adduser student1
# password: password123

Red Hat:
sudo adduser student1
sudo passwd student1
# password: password111

------------------------------------------------------------
✅ 2. Add User to a Group
------------------------------------------------------------

Groups are used to assign collective permissions:

    sudo groupadd developers
    sudo usermod -aG developers student1

Check group membership:

    groups student1

------------------------------------------------------------
✅ 3. Set User Permissions
------------------------------------------------------------

Linux commands help control access and modification rights:
Tools: `chmod`, `chown`, `usermod`

------------------------------------------------------------
⚙️ 4. Giving sudo Privileges
------------------------------------------------------------

To give admin (sudo) privileges:

    sudo usermod -aG sudo student1

Test it:

    su - student1
    sudo apt update

If configured correctly, student1 can run sudo commands.

------------------------------------------------------------
📁 Example: File Permissions
------------------------------------------------------------

Create a project folder:

    mkdir -p project1
    ls -la project1

Sample output:

    drwxr-xr-x 2 student1 student1 4096 May 29 05:52
    drwx------ 3 student1 student1 4096 May 29 05:52

🔐 Permissions: rwxr-xr-x

Split into:
- Owner (student1): rwx = read, write, execute
- Group (student1): r-x = read, execute
- Others: r-x = read, execute

Change ownership and permissions:

    sudo chown student1:developers /home/student1/project1/
    sudo chmod -R 770 /home/student1/project1/

Check updated permissions:

    ls -la project1

Expected:

    drwxrwx--- 2 student1 developers 4096 May 29 05:52 .
    drwx------ 3 student1 student1   4096 May 29 06:00 ..

------------------------------------------------------------
🔧 Commands Explained
------------------------------------------------------------

1. Change owner and group:

   sudo chown student1:developers /home/student1/project1/

- `chown`: change owner
- Owner: student1
- Group: developers

2. Change permissions recursively:

   sudo chmod -R 770 /home/student1/project1/

- Owner (student1): full access
- Group (developers): full access
- Others: no access

------------------------------------------------------------
✅ Create a New User (student2)
------------------------------------------------------------

Add user to groups:

    sudo usermod -aG developers student2
    sudo usermod -aG sudo student2

Switch user:

    su - student2

Try accessing:

    ls -la /home/student1/project1/

Access denied?

Check parent folder:

    ls -ld /home/student1
    # drwx------ 3 student1 student1 4096 May 29 06:00 /home/student1

Only student1 has access.

Fix it:

    sudo chmod 750 /home/student1
    ls -la /home/student1/project1/

Still denied?

    sudo chgrp developers /home/student1
    ls -la /home/student1/project1/

Expected:

    drwxrwx--- 2 student1 developers 4096 May 29 05:52 /home/student1/project1

------------------------------------------------------------
🐳 5. Creating Users Inside a Docker Container
------------------------------------------------------------

Create Dockerfile with `useradd` command

Build Docker image from user-linux directory:

    docker build -t my-linux-image ./user-linux

Run Docker container:

    docker run -it --name linux-container my-linux-image
    id
    whoami

------------------------------------------------------------
🔐 6. Security: Limit Damage from Exploits
------------------------------------------------------------

Running a container as root increases risk:
- Exploits can escalate to host
- Mounted volumes may be exposed

Non-root containers:
- Reduce attack surface
- Are safer by default

------------------------------------------------------------
🧱 7. Principle of Least Privilege
------------------------------------------------------------

Most containers don't need root:
- Give only the permissions needed
- Improves security and isolation

------------------------------------------------------------
💾 8. File Permission Safety (with Volumes)
------------------------------------------------------------

If running as root:
- Can create files owned by root on host
- Host user may lose access

Run as regular user:
- Avoid permission issues
- Safer file handling

------------------------------------------------------------
⚙️ 9. Compatibility with Kubernetes / OpenShift
------------------------------------------------------------

Platforms like OpenShift:
- Disallow root containers by default
- Use non-root images for better compatibility

------------------------------------------------------------
⚠️ 10. When Is Root Acceptable?
------------------------------------------------------------

Use root *only when necessary*:

- Development/debugging
- Privileged tools (e.g. networking)
- Short-lived, sandboxed containers

Even then, **isolate and control** access.

-------------------------
✅ Concepts to Understand
-------------------------
- vCPU (virtual CPU): Represents a thread of a physical core. On GCP, 1 vCPU = 1 hyper-thread of an 
Intel/AMD core
- Memory: The RAM assigned to your VM. More RAM is usually needed for in-memory processes, databases, 
or larger applications

# -----------------------------------------------------------------------------
# 🛰️ Copy folder to remote server
# -----------------------------------------------------------------------------

# - Login to servers and run command: id, pwd
# - This prints user plus home dir
# - Replace server-ip and username and run below command

ansible all \
-i [server-ip], \
-u [username] \
--private-key=~/.ssh/google_compute_engine \
-m ansible.builtin.synchronize \
-a "src=./docker-linux/files dest=/home/[username]/docker-linux/ recursive=yes"

# -----------------------------------------------------------------------------
# 💻 Login to remote server
# -----------------------------------------------------------------------------

# - chmod +x files/setup_and_run_docker.sh
# - ./files/setup_and_run_docker.sh

# -----------------------------------------------------------------------------
# 🛠️ Build Docker image
# -----------------------------------------------------------------------------

docker build -f ./docker-linux/files/Dockerfile.cpu -t cpu-container ./docker-linux/files/
docker build -f ./docker-linux/files/Dockerfile.error -t error-container ./docker-linux/files/

# -----------------------------------------------------------------------------
# 🧪 Run Docker container with CPU and memory limits
# -----------------------------------------------------------------------------

docker run --cpus="0.5" --memory="512m" cpu-container
docker run -p 8080:8080 error-container

# -----------------------------------------------------------------------------
# 📊 Open new terminal and run commands
# -----------------------------------------------------------------------------

# - free -h
# - docker stats
# - Observe container CPU and Memory usage
# - top, htop
# - free -m
# - df -h
# - uname -a
# - whoami
# docker ps
# docker logs container-name







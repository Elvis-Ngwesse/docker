~~☁️ Google Cloud VM Setup
-------------------------

--------------------------------------
🔧 Set Your Default Project and Region
--------------------------------------
gcloud config set project [PROJECT_ID]  
gcloud config set compute/zone europe-west2-a

--------------------------
🖥️ Create the Red Hat VM
--------------------------
gcloud compute instances create rhel-vm \
--image-family rhel-9 \
--image-project rhel-cloud \
--machine-type e2-medium \
--tags http-server,https-server,custom-ports

------------------------
🐧 Create the Debian VM
------------------------
gcloud compute instances create debian-vm \
--image-family debian-12 \
--image-project debian-cloud \
--machine-type e2-medium \
--tags http-server,https-server,custom-ports

-------------------------------------------------
🛡️ Create a Firewall Rule to Open Required Ports
-------------------------------------------------
gcloud compute firewall-rules create allow-custom-ports \
--allow tcp:22,tcp:80,tcp:5000,tcp:8000-9000 \
--target-tags custom-ports \
--description="Allow SSH, HTTP, and custom ports 5000, 8000-9000"

-----------------------
🔐 SSH into Red Hat VM
-----------------------
gcloud compute ssh rhel-vm

----------------------
🔐 SSH into Debian VM
----------------------
gcloud compute ssh debian-vm

--------------
🗑️ Delete VMs
--------------
gcloud compute instances delete rhel-vm --quiet  
gcloud compute instances delete debian-vm --quiet

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

docker build -t cpu-test ./docker-linux/files/

# -----------------------------------------------------------------------------
# 🧪 Run Docker container with CPU and memory limits
# -----------------------------------------------------------------------------

docker run --cpus="0.5" --memory="512m" cpu-test

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







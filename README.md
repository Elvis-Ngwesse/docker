# docker
A repository focused on Docker containers and file handling. Includes Dockerfiles, compose files, and 
examples to build, run, and manage containers efficiently. Ideal for learning containerization and 
managing files within Docker environments.

# 🪟 Install Docker
- Go to the official Docker download page: https://www.docker.com/products/docker-desktop
- docker --version

# ✅ Test Docker
Run a test container
- docker run hello-world

# ✅ Windows
- Open Command Prompt or PowerShell
- Navigate to your project folder
- cd path\to\your\project
- python -m venv venv
- .\venv\Scripts\activate

# ✅ macOS / Linux
- Open Terminal
- Navigate to your project folder
- cd /path/to/your/project
- python3 -m venv venv
- source venv/bin/activate


~~☁️ Google Cloud VM Setup
-------------------------

--------------------------------------
🔧 Set Your Default Project and Region
--------------------------------------
gcloud config set project [PROJECT_ID]  
gcloud config set compute/zone europe-west2-a
gcloud config list

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
gcloud compute firewall-rules delete allow-custom-ports

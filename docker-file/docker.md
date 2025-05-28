🐳 Docker Hands-On Tutorial
---------------------------

---------------------
✅ 1. What is Docker?
---------------------
- Docker is a tool designed to make it easier to create, deploy, and run applications using containers
- Containers are lightweight, portable units that package code and its dependencies
- Containers are faster and more efficient than virtual machines

---------------------
🛠️ 2. Install Docker
---------------------
- Install Docker from: https://docs.docker.com/get-docker/
- docker --version

------------------------------
📁 3. Create Docker Container
------------------------------
# Print
- docker build -t print-app .
- docker run --rm print-app

# Api
- pip install flask pandas
- docker build -t top-cities .
- docker run --name top-cities-container -p 9000:9000 top-cities
- Navigate to http://127.0.0.1:9000
- Enter country name

-----------------------------
🔍 4. Monitor Resource Usage
-----------------------------
- docker stats
- docker top top-cities-container
- docker exec -it top-cities-container bash
  - ls -la
- cat /etc/os-release

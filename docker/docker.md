
🐳 Docker Hands-On Tutorial 

✅ 1. What is Docker?
- Docker is a tool designed to make it easier to create, deploy, and run applications using containers
- Containers are lightweight, portable units that package code and its dependencies
- Containers are faster and more efficient than virtual machines

🛠️ 2. Install Docker
- Install Docker from: https://docs.docker.com/get-docker/
- docker --version

📁 3. Create Docker container
# Print
- docker build -t print-app .
- docker run --rm print-app

# Api
- pip install flask pandas
- docker build -t flask-top-cities .
  docker run -p 9000:9000 flask-top-cities

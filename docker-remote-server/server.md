# Create server (all commands are in readme.md)
--------------------------------------------------
- create either red hat or debian machine
- open server ports
- Login and get username
- whoami

# 🧳 Copy Folder to Remote Server
--------------------------------------------------
- gcloud compute scp --zone=europe-west2-a --recurse docker-remote-server [username]@[machine-name]:/home/[username]

# -----------------------------------------------------------------------------
# 💻 Execute command on remote server
# -----------------------------------------------------------------------------
- gcloud compute ssh [machine-name] --zone=europe-west2-a --command="chmod +x ~/docker-remote-server/setup_and_run_docker.sh"
  <!-- Make the setup script executable -->

- gcloud compute ssh [machine-name] --zone=europe-west2-a --command="script -q -c '~/docker-remote-server/setup_and_run_docker.sh' /tmp/session.log"
  <!-- Run the setup script and save output to session.log -->

- gcloud compute ssh [machine-name] --zone=europe-west2-a --command="cat /tmp/session.log"
  <!-- View the output of the setup script -->

- gcloud compute ssh [machine-name] --zone=europe-west2-a --command="cd ~/docker-remote-server && docker compose up --build --force-recreate -d"
  <!-- Build and start Docker containers in detached mode -->

- gcloud compute ssh rhel-vm --zone=europe-west2-a --command="docker ps"
  <!-- List running Docker containers -->

- gcloud compute ssh rhel-vm --zone=europe-west2-a --command="docker logs my-nginx"
  <!-- Show logs from the 'my-nginx' container -->

# 🌐 Access Nginx from Your Local Machine
--------------------------------------------------
From your local browser, visit:
http://server-ip:8080
<!-- Replace server-ip with your actual server IP address -->


# 📁 Managing Images and Cleanup
--------------------------------------------------
- docker stop $(docker ps -q)
- docker rm $(docker ps -aq)
- docker rmi $(docker images -q)
- docker volume rm $(docker volume ls -q)
- docker system prune (cleans up unused data to free up space)


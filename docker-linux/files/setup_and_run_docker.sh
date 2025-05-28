#!/bin/bash

# -----------------------------------------------------------------------------
# 🚀 Docker Setup and Container Run Script for Debian and RHEL 9.6
# -----------------------------------------------------------------------------
# This script handles:
#   - Docker installation (for Debian and RHEL)
#   - Rsync and Htop installation
#   - Building a Docker image from a directory
#   - Running a container with memory and CPU limits
# -----------------------------------------------------------------------------

# Detect OS
OS=$(source /etc/os-release && echo "$ID")

echo "Detected OS: $OS"

# -----------------------------------------------------------------------------
# 🔧 1. Install Docker, Rsync, and Htop based on OS
# -----------------------------------------------------------------------------

if [[ "$OS" == "debian" ]]; then
    echo "Installing Docker, rsync, and htop on Debian..."

    sudo apt update
    sudo apt install -y ca-certificates curl gnupg rsync htop

    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/debian/gpg | \
      sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg

    echo \
      "deb [arch=$(dpkg --print-architecture) \
      signed-by=/etc/apt/keyrings/docker.gpg] \
      https://download.docker.com/linux/debian \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    sudo apt update
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

elif [[ "$OS" == "rhel" ]]; then
    echo "Installing Docker, rsync, and htop on RHEL..."

    sudo dnf install -y rsync htop
    sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
    sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
else
    echo "❌ Unsupported OS: $OS"
    exit 1
fi

# -----------------------------------------------------------------------------
# 🔄 2. Start Docker and Enable on Boot
# -----------------------------------------------------------------------------
echo "Starting and enabling Docker..."
sudo systemctl enable --now docker

# -----------------------------------------------------------------------------
# 👤 3. Add current user to Docker group (optional)
# -----------------------------------------------------------------------------
echo "Adding current user to the docker group..."
sudo usermod -aG docker $USER

# Apply group change in current shell (optional for interactive)
if [[ $- == *i* ]]; then
    newgrp docker
else
    echo "ℹ️  Run 'newgrp docker' or log out and back in for group changes to take effect."
fi

# -----------------------------------------------------------------------------
# ✅ Done
# -----------------------------------------------------------------------------
echo "✅ All done. Docker, rsync, and htop are installed."

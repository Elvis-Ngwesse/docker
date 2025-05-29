FROM ubuntu:22.04

# Install sudo and create non-root user
RUN apt-get update && apt-get install -y sudo \
    && useradd -ms /bin/bash studentuser \
    && echo "studentuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to non-root user
USER studentuser
WORKDIR /home/studentuser

# Start with an interactive shell
CMD ["/bin/bash"]

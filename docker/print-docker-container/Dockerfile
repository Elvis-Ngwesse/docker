# Start from the official slim Python image
FROM python:3.11-slim

# Prevent .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user and home directory
RUN adduser --disabled-password --gecos '' appuser

# Set working directory
WORKDIR /home/appuser/app

# Copy project files and give ownership to appuser
COPY . /home/appuser/app
RUN chown -R appuser:appuser /home/appuser/app

# Switch to the non-root user
USER appuser

# Set default command
CMD ["python", "print-app.py"]


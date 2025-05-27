# Use official Python image
FROM python:3.11-slim

# Create a non-root user
RUN adduser --disabled-password --gecos '' flaskuser

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Change ownership of the app folder
RUN chown -R flaskuser:flaskuser /app

# Switch to non-root user
USER flaskuser

# Expose port
EXPOSE 9000

# Run the app
CMD ["python", "api-app.py"]

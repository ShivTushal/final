FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    procps \          # For process management
    podman \          # Podman client
    at \              # For scheduling commands
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies directly
RUN pip install --no-cache-dir \
    flask \           # Web framework
    python-dotenv \   # Environment variables
    gunicorn          # Production WSGI server

WORKDIR /app

# Copy application files
COPY . .

# Create directory for logs and make it writable
RUN mkdir -p /tmp && chmod a+rwx /tmp

# Create directory for Podman sockets
RUN mkdir -p /run/podman && chmod a+rwx /run/podman

# Ensure the start script is executable
RUN chmod +x /host_scripts/start-container.sh

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the application port
EXPOSE 8000

# Start the application with Gunicorn (production)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]

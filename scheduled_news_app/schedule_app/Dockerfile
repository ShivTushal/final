FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    procps \
    podman \
    at \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir flask gunicorn

WORKDIR /app

# Create required directories
RUN mkdir -p /host_scripts /tmp && \
    chmod a+rwx /tmp && \
    mkdir -p /run/podman

COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 8000

# Start services and application
CMD service atd start && \
    gunicorn --bind 0.0.0.0:8000 --workers 4 app:app

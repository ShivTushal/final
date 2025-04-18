FROM python:3.10-slim

WORKDIR /app

# Copy only schedule.py (do NOT copy start-container.sh anymore)
COPY schedule.py .

# Install Flask and atd (scheduling daemon)
RUN apt-get update && \
    apt-get install -y at && \
    pip install flask

# Start the at daemon and run the Flask app
CMD ["sh", "-c", "service atd start && python schedule.py"]

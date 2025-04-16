
FROM python:3.10-slim
WORKDIR /app
COPY schedule.py start-container.sh ./
RUN chmod +x start-container.sh && pip install flask
CMD ["python", "schedule.py"]


FROM python:3.10-slim
WORKDIR /app
COPY app.py ./app.py
COPY templates/ ./templates/
RUN pip install flask requests
CMD ["python", "app.py"]

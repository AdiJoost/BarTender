FROM python:3.9-slim
WORKDIR /ProjectTemplate
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "run.py"]
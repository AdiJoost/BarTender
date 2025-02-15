FROM python:3.9-slim
WORKDIR /BarTender
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 6969
COPY . .
CMD ["python", "run.py"]
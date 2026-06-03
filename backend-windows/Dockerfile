FROM python:3.11-slim

WORKDIR /opt/jarvis

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV JARVIS_HOST=0.0.0.0
ENV JARVIS_PORT=8000
ENV JARVIS_DEBUG=false
ENV PYTHONPATH=/opt/jarvis

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

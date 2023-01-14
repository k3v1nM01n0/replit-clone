FROM python:3.9-slim

COPY . /replit-clone

WORKDIR /replit-clone

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5004

CMD ["python", "replit.py"]

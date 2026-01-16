
FROM python:3.9-slim
WORKDIR /app
RUN pip install --no-cache-dir Pillow
COPY scraper.py .
RUN mkdir images
CMD ["python", "scraper.py"]
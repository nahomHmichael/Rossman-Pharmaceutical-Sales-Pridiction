# Dockerfile, image, container
FROM python:3.9-slim
COPY requirement.txt .
RUN python -m pip install -r requirement.txt
RUN apt-get update -y
WORKDIR /app
COPY . /app
RUN pip intall -r requirement.txt
EXPOSE 8501
CMD ["python","dashboard/app.py"]


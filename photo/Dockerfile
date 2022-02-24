# Pull the official base image
FROM python:3.6

# Set environmental variables
ENV TZ = Europe/Warsaw
ENV PYTHONUNBUFFERED=1

# Set work directory (from which our application will be launched)
WORKDIR /code/

# Docker installs our dependencies on the container
COPY requirements.txt /code/

# Update and install application's dependencies
# RUN executes commands in terminal while building the image
RUN apt-get update  && apt-get install -y
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy all project (from our directory to the Docker)
COPY . /code/

# pull official base image - The project uses python 3.8.10 version
FROM python:3.8.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set work directory
WORKDIR /code

RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc \
                                        libsndfile1

# install dependencies
RUN pip install --upgrade pip

# Copy requirements.txt file to the working directory
COPY requirements.txt /code/


RUN pip install --no-cache-dir -r requirements.txt


# copy project
COPY . /code/
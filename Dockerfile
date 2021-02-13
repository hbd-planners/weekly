# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code/weekly

# Install dependencies
COPY Pipfile Pipfile.lock /code/weekly/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/weekly/


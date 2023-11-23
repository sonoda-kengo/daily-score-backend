FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs

WORKDIR /code
COPY . /code/

# pip
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv sync --system --dev
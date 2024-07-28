FROM python:3.11.9-slim
LABEL maintainer="Ibrahim Al-shami <alshamiibrahim96@gmail.com>"

# Set work directory
WORKDIR /app

ARG UID=1000
ARG GID=1000


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DEFAULT_TIMEOUT=100


# Update packages and install necessary dependencies
RUN apt update -y && \
    apt install -y software-properties-common python3-numpy \
    libpq-dev build-essential libssl-dev \
    zlib1g-dev libncurses5-dev libncursesw5-dev \
    libreadline-dev libsqlite3-dev libgdbm-dev \
    libdb5.3-dev libbz2-dev libexpat1-dev \
    liblzma-dev tk-dev libffi-dev unixodbc-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    groupadd -g "${GID}" python && \
    useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python


# Switch to python user
USER python

# Add user-local bin directory to PATH
ENV PATH="/home/python/.local/bin:${PATH}"

# Install pip-tools
RUN pip install pip-tools && \
    pip install --upgrade pip && \
    which pip-sync && \
    pip-sync --version

# copy project and requirements and install dependencies
ARG BACKEND_PATH=.
ARG REQUIREMENTS=local

COPY --chown=python:python $BACKEND_PATH/requirements/ /app/requirements/
RUN cd /app/requirements && \
    pip-sync $REQUIREMENTS.txt
COPY --chown=python:python $BACKEND_PATH /app

# Creates default super user and run migrate
RUN chmod +x /app/scripts/*.sh

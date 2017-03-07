FROM resin/rpi-raspbian:jessie
MAINTAINER Govinda Fichtner <govinda@hypriot.com>

# Install dependencies
RUN apt-get update && apt-get install -y \
    git-core \
    build-essential \
    gcc \
    python \
    python-dev \
    python-pip \
    python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pyserial
RUN git clone git://git.drogon.net/wiringPi
RUN cd wiringPi && ./build
RUN pip install wiringpi2
#----------hier nun Teile des autobahn Dockerfiles

ENV HOME /app
ENV DEBIAN_FRONTEND noninteractive

# Crossbar.io connection defaults
ENV CBURL ws://104.199.76.81:8080/ws
ENV CBREALM realm1

# install Autobahn|Python
RUN pip install -U pip && pip install autobahn[asyncio]

RUN pip install trollius

RUN pip install pyserial
RUN pip install adafruit_python_dht
RUN pip install pyserial
RUN pip install gpiozero
RUN pip install pause
# add example service
COPY ./app /app

# make /app a volume to allow external configuration
VOLUME /data
VOLUME /app

# set the app component directory as working directory
WORKDIR /app
#WORKDIR /data


# run service entry script by default
CMD ["sh", "/app/run"]


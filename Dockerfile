FROM selenium/standalone-chrome:91.0

USER root
RUN apt-get update
RUN apt-get install -y python3-pip

RUN pip3 install requests

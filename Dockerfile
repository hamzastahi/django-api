#FROM python:3
#ENV PYTHONUNBUFFERED 1
#RUN mkdir /code
#WORKDIR /code
#COPY ./ /code/
#RUN apt-get update -y && \
#   apt-get install python3-venv \
#                   python3-pip
# Installing Django and Django Rest Framework
# RUN pip3 install django \
#                 djangorestframework

# base image to be used
FROM python:3.6
# The environment variable ensures that the python output is set 
#straight to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code

# add the requirements file to the working dir
COPY requirements.txt /code/

#install the requirements (install before adding rest of code to #avoid rerunning this at every code change-built in layers)
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/

#set environment vars to be used
#ENV AUTHOR="Mokgadi"
#port from the container to expose to host
EXPOSE 8080
#Tell image what to do when it starts as a container
CMD /code/start.sh




FROM python:3.8
# set the base image. Since we're running
# a Python application a Python base image is used FROM python:3.8
# set a key-value label for the Docker image
LABEL maintainer="Kaveh Kasaee"
# copy files from the host to the container filesystem. 
# For example, all the files in the current directory
# to the  `/streamlit` directory in the container
COPY . /streamlit
#  defines the working directory within the container
WORKDIR /streamlit
# run commands within the container. 
# For example, invoke a pip command 
# to install dependencies defined in the requirements.txt file. 
RUN pip install -r requirements.txt
# provide a command to run on container start. 
# For example, start the `dashboard.py` application.
EXPOSE 5111
CMD [ "streamlit", "run", "main.py","--server.port","5111" ]
# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /flask_app

# Copy the current directory contents into the container at /app
ADD . /flask_app

# Install the dependencies
RUN pip install -r requirements.txt

ENV USER_NAME='eduardo'
ENV USER_PASS='teste'

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
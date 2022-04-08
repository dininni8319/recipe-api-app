FROM python:3.7-alpine
MAINTAINER London App Developer Ltd

#Tells PYTHON to run  UNBUFFERED mode, prints the output directly, to avoid complecation with the docker image
ENV PYTHONUNBUFFERED 1 
# copies the requirements into the image
COPY ./requirements.txt /requirements.txt
#installs the requirements
RUN pip install -r /requirements.txt

#create an empty folder on a docker image and then it switchs as default directory
RUN mkdir /app
WORKDIR /app 
#The next step it copy the app from are folder into are docker image
COPY ./app /app

#We create a user that is going to run are application 
#here we create a user that is going to run the application only 
#In the line 22 docker switchs to the new create user
#This is done for security reason
RUN adduser -D user
USER user 
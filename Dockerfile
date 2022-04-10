FROM python:3.7-alpine
MAINTAINER London App Developer Ltd

#Tells PYTHON to run  UNBUFFERED mode, prints the output directly, to avoid complecation with the docker image
ENV PYTHONUNBUFFERED 1 
# copies the requirements into the image
COPY ./requirements.txt /requirements.txt
# we are going to install the postgressql client 
#apk is the name of the package manager, updates the registry before we add it, no-cache means don't store the registry index on aree docker file, to minimaze the packages and files in our docker container 
RUN apk add --update --no-cache postgresql-client
#temporary packages that need to be installed when we run our requirements and we remove after the 
#installs the requirements
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt
#here we are removing the temporary requirements
#run docker-build to install the dependencies
RUN apk del .tmp-build-deps
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
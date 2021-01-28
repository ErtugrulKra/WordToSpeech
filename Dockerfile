FROM python

# set the working directory in the container
WORKDIR /

# copy the dependencies file to the working directory
COPY installs.txt .

RUN apt-get update && apt-get upgrade -y
RUN apt-get install espeak -y
RUN apt-get install ffmpeg -y
RUN apt-get install libespeak1 -y

# install dependencies
RUN pip3 install -r installs.txt

# copy the content of the local src directory to the working directory
COPY ./ .

EXPOSE 5000

# command to run on container start
CMD [ "python", "./wordtospeech.py" ]
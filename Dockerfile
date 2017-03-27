FROM alpine:3.1 
MAINTAINER Zach Kontoulis <z.kontoulis@gmail.com>

# Update
RUN apk add --update python py-pip 

COPY . / 
# Install app dependencies
RUN pip install -r /requirements.txt

CMD ["python", "/updater.py"]


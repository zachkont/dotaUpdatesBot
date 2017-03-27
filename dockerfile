FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install -r requirements.txt

# Bundle app source
COPY test.py /src/test.py

EXPOSE  8000
CMD ["python", "/src/test.py", "-p 8000"]

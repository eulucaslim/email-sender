FROM miigotu/python3.11

WORKDIR /email-sender
COPY ./ ./

RUN pip install -r /email-sender/requirements.txt
EXPOSE 8000
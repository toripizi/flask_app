FROM python:3.10.13-bookworm

COPY requirements.txt .
RUN pip install --requirement requirements.txt

RUN cd /opt && mkdir ctf
WORKDIR /opt/ctf



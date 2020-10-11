FROM ubuntu:20.04
FROM python:3.8
RUN pip3 install --upgrade pip
RUN pip3 install pytest sklearn
COPY eg eg/
COPY test test/.
COPY search search/.
ENV PYTHONPATH .
FROM ubuntu:19.10
RUN apt update
RUN apt install -y python3 python3-pip ipython3
RUN pip3 install networkx numpy scipy pandas matplotlib community
RUN mkdir py
WORKDIR /py
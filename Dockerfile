FROM ubuntu:latest
LABEL authors="Jo"

ENTRYPOINT ["top", "-b"]
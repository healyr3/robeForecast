FROM ubuntu:latest
LABEL authors="Ross"

ENTRYPOINT ["top", "-b"]

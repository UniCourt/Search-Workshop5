FROM public.ecr.aws/docker/library/python:3.10

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ENV API_HOST 127.0.0.1

COPY ./src ./src

WORKDIR src

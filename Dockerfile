FROM python:3.7-alpine3.10
MAINTAINER v.stone@163.com
WORKDIR /workspace
COPY . .
RUN pip install requirements.txt 
CMD launch.sh
EXPOSE 3000
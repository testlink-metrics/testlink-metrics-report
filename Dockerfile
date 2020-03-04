FROM python:3.7-alpine3.10
MAINTAINER v.stone@163.com
WORKDIR /workspace
COPY . .
RUN pip install -r requirements.txt 
CMD /workspace/launch.sh
EXPOSE 6080

# TestLink Metrics Report Tool
> Open source software for TestLink metrics. 

[![org](https://img.shields.io/badge/org-truth%20%26%20insurance%20workshop-informational)](http://bx.baoxian-sz.com)
![author](https://img.shields.io/badge/author-v.stone@163.com-informational)
![github](https://img.shields.io/github/license/testlink-metrics/testlink-metrics-report)
[![docker](https://img.shields.io/badge/build-docker-informational)](https://hub.docker.com/r/bxwill/testlink-metrics)
![flask](https://img.shields.io/badge/framework-flask-success)
![bootstrap](https://img.shields.io/badge/toolkit-bootstrap-success)
![element](https://img.shields.io/badge/icon-element-success)


We hope `EASY METRICS EASY MANAGEMENT`

#### Quick Start
```bash
export TESTLINK_URL=''
export TESTLINK_USER=''
export TESTLINK_DEVKEY=''
docker run -d -p 80:80 -e TESTLINK_URL:${TESTLINK_URL} -e TESTLINK_USER:${TESTLINK_USER} -e TESTLINK_DEVKEY:${TESTLINK_DEVKEY} -it bxwill/testlink-metrics
```
or you can leverage `docker-compose`
```bash
docker-compose -f docker-compose.yaml
```
variable `ISSUE_TRACKER_URI_VIEW` is optional

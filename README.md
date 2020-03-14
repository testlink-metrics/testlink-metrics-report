# TestLink Metrics Report Tool
> Open source software for TestLink metrics. 

[![org](https://img.shields.io/static/v1?style=for-the-badge&label=org&message=Truth%20%26%20Insurance%20Workshop&color=597ed9)](http://bx.baoxian-sz.com)
![author](https://img.shields.io/static/v1?style=for-the-badge&label=author&message=v.stone@163.com&color=blue)
![github](https://img.shields.io/github/license/testlink-metrics/testlink-metrics-report?style=for-the-badge)
[![alpine](https://img.shields.io/static/v1?style=for-the-badge&logo=alpine%20linux&label=Alpine%20Linux&message=3.10&color=0D597F)](https://www.alpinelinux.org)
[![python](https://img.shields.io/static/v1?style=for-the-badge&logo=python&label=Python&message=3.7&color=3776AB)](https://www.python.org)
[![docker](https://img.shields.io/static/v1?style=for-the-badge&logo=docker&label=docker&message=bxwill/testlink-metrics&color=2496ED)](https://hub.docker.com/r/bxwill/testlink-metrics)
![flask](https://img.shields.io/static/v1?style=for-the-badge&logo=python&label=flask&message=1.1.1&color=3776AB)
[![bootstrap](https://img.shields.io/static/v1?style=for-the-badge&logo=bootstrap&label=bootstrap&message=v4&color=563D7C)](https://v4.bootcss.com)
[![element](https://img.shields.io/static/v1?style=for-the-badge&logo=css3&label=element&message=2.13.0&color=1572B6)](https://element.eleme.cn/#/en-US/component/icon)
[![testlink](https://img.shields.io/static/v1?style=for-the-badge&logo=php&label=testlink&message=1.9.x&color=777BB4)](https://github.com/TestLinkOpenSourceTRMS/testlink-code)


We hope `EASY METRICS EASY MANAGEMENT`

## Quick Start
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

![TestLinkMetricsReportPreview](preview.png)

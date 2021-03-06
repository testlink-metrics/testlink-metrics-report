# TestLink Metrics Report Tool
##### English | [中文](README.cn.md)

> Open source software for TestLink metrics

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

## Vision

**EASY METRICS EASY MANAGEMENT**

## Description

TestLink Metrics Report `TMR` can help to manage test case execution status, and login TestLink is not necessary. 
You can choose `Project` `Plan` `Build` `Platform` `Requiment` to generate a HTML report. 
`Progress` `Executed Results` `Rate` `Case List` `Bug List` can be found from the report.

## Quick Start

#### Deploy TMR
```bash
export TESTLINK_URL: ''      # Required: URL of TestLink
export TESTLINK_USER: ''     # Required: Username in TestLink
export TESTLINK_DEVKEY: ''   # Required: Dev Key of the TestLink Username
export TESTLINK_ITS: ''      # Optional: Issue Tracker System Name in TestLink
docker run -d -p 80:80 -e TESTLINK_URL:${TESTLINK_URL} -e TESTLINK_USER:${TESTLINK_USER} -e TESTLINK_DEVKEY:${TESTLINK_DEVKEY} -it bxwill/testlink-metrics
```
or you can leverage `docker-compose`
```bash
docker-compose -f docker-compose.yaml up -d
```
variable `TESTLINK_ITS` is optional

#### Access TMR
`http://localhost`
![TestLinkMetricsReportPreview](https://repository-images.githubusercontent.com/247091078/962f8200-6aa7-11ea-881b-0a2a3781be33)

## Changelog

- 1.2.1 - `2020-05-08`
> - Enhance case executed status table 
> - Update top right corner GitHub link

- 1.2.0 - `2020-05-05`
> - Improve case page to show executed results
> - Get issue tracker URI view via TestLink ITS
> - Enhance html templates

- 1.1.1 - `2020-04-28`
> - Fix case page css path error

- 1.1.0 - `2020-04-26`
> - Support to print view test case detail
> - Fix no-platform scenario failure

- 1.0.0 - `2020-03-20`
> - Select project/plan/build/platform to generate report
> - Testing progress and results can be found from the report
> - Requirement coverage and progress can be found from the report
> - List case title, result 
> - Bugs and links will be displayed if configured issue tracker uri view

## More
- GitHub: https://github.com/testlink-metrics/testlink-metrics-report
- Docker: https://hub.docker.com/r/bxwill/testlink-metrics

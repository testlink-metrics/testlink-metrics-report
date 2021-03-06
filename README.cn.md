# TestLink Metrics Report Tool
##### [English](README.md) | 中文

> TestLink 指标报告开源项目

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

## 愿景

**简单度量，简单管理**

## 简介

TestLink Metrics Report `TMR` 可以在不登录 TestLink 的情况下，查看测试用例执行结果的情况，并且可以通过选择 `测试项目` `测试计划` `测试版本` `测试平台` `测试需求` 来生成网页版的报告。
在报告中可以查看 `测试进度` `测试用例执行结果` `比例` `用例列表` `缺陷列表`。

## 快速开始

#### 安装 TMR
```bash
export TESTLINK_URL: ''      # 必须的: TestLink 地址
export TESTLINK_USER: ''     # 必须的: TestLink 中的账号
export TESTLINK_DEVKEY: ''   # 必须的: TestLink Username
export TESTLINK_ITS: ''      # 可选的: Issue Tracker System Name in TestLink
docker run -d -p 80:80 -e TESTLINK_URL:${TESTLINK_URL} -e TESTLINK_USER:${TESTLINK_USER} -e TESTLINK_DEVKEY:${TESTLINK_DEVKEY} -it bxwill/testlink-metrics
```
或者你也可以使用 `docker-compose`
```bash
docker-compose -f docker-compose.yaml up -d
```
变量 `TESTLINK_ITS` 是可选的。

#### 访问 TMR
`http://localhost`
![TestLinkMetricsReportPreview](https://repository-images.githubusercontent.com/247091078/962f8200-6aa7-11ea-881b-0a2a3781be33)

## 版本记录

- 1.2.1 - `2020-05-08`
> - 优化用例执行状态的表格
> - 修改右上角 GitHub 链接

- 1.2.0 - `2020-05-05`
> - 增强测试用例展示页面，显示执行结果
> - 从 TestLink 通过 ITS 自动获取 issue tracker URI view
> - 优化 HTML 模板

- 1.1.1 - `2020-04-28`
> - 修复用例详情页CSS引用路径错误问题

- 1.1.0 - `2020-04-26`
> - 展示测试用例详细内容
> - 修复测试计划无测试平台场景下的错误

- 1.0.0 - `2020-03-20`
> - 选择项目、计划、版本、平台来生成报告
> - 报告包含测试进度和结果
> - 报告中可以查看需求覆盖率和进度
> - 展示测试用例的标题和执行结果
> - 如果配置了缺陷追踪，可以展示用例对应的缺陷及缺陷链接

## 更多
- GitHub: https://github.com/testlink-metrics/testlink-metrics-report
- Docker: https://hub.docker.com/r/bxwill/testlink-metrics

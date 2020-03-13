#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import logging
from metrics.svc.tmr_client import TMRClient


logging.basicConfig(level=logging.INFO, format='[ %(asctime)s ] %(levelname)s %(message)s')

app = Flask(__name__)
tmrclient = TMRClient()


@app.route('/')
def index():
    project_id = request.args.get('project_id')
    plan_id = request.args.get('plan_id')
    build_id = request.args.get('build_id')
    platform_id = request.args.get('platform_id')
    case_id = request.args.get('case_id')
    req_id = request.args.get('req_id')
    report = request.args.get('report')
    return render_template(
        'index.html',
        tmr_version=tmrclient.version,
        project_id=project_id,
        plan_id=plan_id,
        build_id=build_id,
        platform_id=platform_id,
        case_id=case_id,
        req_id=req_id,
        projects=tmrclient.list_project(),
        plans=tmrclient.list_plan(project_id=project_id),
        builds=tmrclient.list_build(plan_id=plan_id),
        platforms=tmrclient.list_platform(plan_id=plan_id),
        summary=tmrclient.get_summary(project_id=project_id,
                                      plan_id=plan_id,
                                      build_id=build_id,
                                      platform_id=platform_id,
                                      req_id=req_id,
                                      report=report)
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

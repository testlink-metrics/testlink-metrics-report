#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
import connexion
import logging
import requests
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
    suite_id = request.args.get('suite_id')
    case_id = request.args.get('case_id')
    return render_template(
        'index.html',
        tmr_version = tmrclient.version,
        project_id = project_id,
        plan_id = plan_id,
        build_id = build_id,
        platform_id = platform_id,
        suite_id = suite_id,
        case_id = case_id,
        projects = tmrclient.list_project(),
        plans = tmrclient.list_plan(project_id=project_id) if project_id else {},
        builds = tmrclient.list_build(plan_id=plan_id) if plan_id else {},
        platforms = tmrclient.list_platform(plan_id=plan_id) if plan_id else {},
        summary = tmrclient.get_summary(project_id=project_id, plan_id=plan_id, build_id=build_id, platform_id=platform_id)
    )


if __name__ == '__main__':
    app.run(port=3000, debug=True)
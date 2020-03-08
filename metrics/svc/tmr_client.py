#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TestlinkApiClient.tlxmlrpc import TestlinkClient
import os


class TMRClient(object):
    def __init__(self):
        self.version = 'TMRv1.0'
        self.tl_url = os.getenv('TESTLINK_URL')
        self.tl_user = os.getenv('TESTLINK_USER')
        self.tl_dev_key = os.getenv('TESTLINK_DEVKEY')
        self.testlink = TestlinkClient(self.tl_url, self.tl_user, self.tl_dev_key)
        self.projects = dict()
        self.plans = dict()
        self.builds = dict() 
        self.platforms = dict() 
        self.summary = dict()
    
    def list_project(self):
        projects = dict()
        try:
            for pid, pname in self.testlink.list_project().items():
                projects[pid] = pname
        except Exception as e:
            print(e)
        return projects
    
    def list_plan(self, project_id):
        plans = dict()
        try:
            for pid, pname in self.testlink.list_plan(project_id=project_id).items():
                plans[pid] = pname
        except Exception as e:
            print(e)
        return plans

    def list_build(self, plan_id):
        builds = dict()
        if plan_id:
            try:
                builds = self.testlink.list_build(plan_id=plan_id)
            except Exception as e:
                print(e)
        return builds

    def list_platform(self, plan_id):
        platforms = dict()
        if plan_id:
            try:
                platforms = self.testlink.list_platform(plan_id=plan_id)
            except Exception as e:
                print(e)
        return platforms 

    def get_summary(self, project_id=None, plan_id=None, build_id=None, platform_id=None):
        summary = {
            'total': 0,
            'executed': 0,
            'executed_rate': 0,
            'pass': 0,
            'pass_rate': 0,
            'fail': 0,
            'fail_rate': 0,
            'block': 0,
            'block_rate': 0,
            'notrun': 0,
            'notrun_rate': 0,
            'case': dict()
        }
        if project_id and plan_id:
            try:
                _data = self.testlink.get_report_for_plan(project_id=project_id, plan_id=plan_id, build_id=build_id, platform_id=platform_id)
                summary['total'] = sum([_data['pass'], _data['fail'], _data['block'], _data['notrun']])
                summary['executed'] = sum([_data['pass'], _data['fail'], _data['block']])
                summary['executed_rate'] = 0 \
                    if summary['total'] == 0 \
                    else '%.2f' % float(summary['executed']/summary['total']*100)
                summary['pass'] = _data['pass']
                summary['pass_rate'] = 0 \
                    if summary['executed'] == 0 \
                    else '%.2f' % float(_data['pass']/summary['executed']*100)
                summary['pass_total_rate'] = 0 \
                    if summary['total'] == 0 \
                    else '%.2f' % float(_data['pass'] / summary['total'] * 100)
                summary['fail'] = _data['fail']
                summary['fail_rate'] = 0 \
                    if summary['executed'] == 0 \
                    else '%.2f' % float(_data['fail']/summary['executed']*100)
                summary['fail_total_rate'] = 0 \
                    if summary['total'] == 0 \
                    else '%.2f' % float(_data['fail']/summary['total']*100)
                summary['block'] = _data['block']
                summary['block_rate'] = 0 \
                    if summary['executed'] == 0 \
                    else '%.2f' % float(_data['block']/summary['executed']*100)
                summary['block_total_rate'] = 0 \
                    if summary['total'] == 0 \
                    else '%.2f' % float(_data['block']/summary['total']*100)
                summary['notrun'] = _data['notrun']
                summary['notrun_rate'] = 0 \
                    if summary['total'] == 0 \
                    else '%.2f' % float(_data['notrun']/summary['total']*100)
                summary['case'] = _data['case']
            except Exception as e:
                print(e)
        return summary
    
    def get_requirement(self):
        pass


if __name__ == '__main__':
    print('This TMR Client')

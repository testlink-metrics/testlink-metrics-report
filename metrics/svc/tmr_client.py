#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Will v.stone@163.com

from TestlinkApiClient.tlxmlrpc import TestlinkClient
import os
import logging
import inspect


class TMRClient(object):
    def __init__(self):
        self.version = 'TMRv1.2'
        self.tl_url = os.getenv('TESTLINK_URL')
        self.tl_user = os.getenv('TESTLINK_USER')
        self.tl_dev_key = os.getenv('TESTLINK_DEVKEY')
        self.testlink = TestlinkClient(self.tl_url, self.tl_user, self.tl_dev_key)
        if os.getenv('TESTLINK_ITS'):
            self.issue_tracker_uri_view = self.testlink.get_issue_tracker(os.getenv('TESTLINK_ITS')).get('uriview')
        else:
            self.issue_tracker_uri_view = ''

    def list_project(self):
        """
        List Project
        :return:
            {project_id: project_name}
        """
        projects = dict()
        try:
            for pid, pname in self.testlink.list_project().items():
                projects[pid] = pname
        except Exception as e:
            logging.warning("[ %s %s ] %s" % (__name__, inspect.stack()[0][3], e))
        return projects
    
    def list_plan(self, project_id):
        """
        List Plan
        :param project_id:
        :return:
            {plan_id: plan_name}
        """
        plans = dict()
        if project_id:
            try:
                for pid, pname in self.testlink.list_plan(project_id=project_id).items():
                    plans[pid] = pname
            except Exception as e:
                logging.warning("[ %s %s ] %s" % (__name__, inspect.stack()[0][3], e))
        return plans

    def list_build(self, plan_id):
        """
        List Build
        :param plan_id:
        :return:
            {build_id: build_name}
        """
        builds = dict()
        if plan_id:
            try:
                builds = self.testlink.list_build(plan_id=plan_id)
            except Exception as e:
                logging.warning("[ %s %s ] %s" % (__name__, inspect.stack()[0][3], e))
        return builds

    def list_platform(self, plan_id):
        """
        List Platform
        :param plan_id:
        :return:
            {platform_id: platform_name}
        """
        platforms = dict()
        if plan_id:
            try:
                platforms = self.testlink.list_platform(plan_id=plan_id)
            except Exception as e:
                logging.warning("[ %s %s ] %s" % (__name__, inspect.stack()[0][3], e))
        return platforms

    def list_requirement(self, project_id: str, plan_id: str):
        """
        Requirement List
        :param project_id:
        :param plan_id:
        :return:
            {req_id: req_doc_id}
        """
        requirements = dict()
        if project_id and plan_id:
            requirements = self.testlink.list_requirement(project_id=project_id, plan_id=plan_id)
        return requirements

    def get_case(self, project_id: str, plan_id: str, case_ext_id: str, build_id=None, platform_id=None):
        case_detail = self.testlink.get_case(project_id=project_id, case_ext_id=case_ext_id)
        case_exec_results = self.testlink._get_last_execution_result(project_id=project_id,
                                                                     plan_id=plan_id,
                                                                     build_id=build_id,
                                                                     platform_id=platform_id,
                                                                     case_ext_id=case_ext_id)
        case_info = {
            'ext_id': case_detail[0].get('full_tc_external_id'),
            'name': case_detail[0].get('name'),
            'summary': case_detail[0].get('summary'),
            'preconditions': case_detail[0].get('preconditions'),
            'steps': case_detail[0].get('steps'),
            'exec_plan': self.testlink.list_plan(project_id=project_id).get(plan_id),
            'exec_build': self.testlink.list_build(project_id=project_id, plan_id=plan_id).get(build_id),
            'exec_platform': self.testlink.list_platform(project_id=project_id, plan_id=plan_id).get(platform_id),
            'exec_status': case_exec_results[0].get('status'),
            'exec_notes': case_exec_results[0].get('notes'),
            'exec_bugs': case_exec_results[0].get('bugs'),
            'issue_tracker_uri': self.issue_tracker_uri_view,
        }
        return case_info

    def get_summary(self, project_id=None, plan_id=None, build_id=None, platform_id=None, req_id=None, report=''):
        """
        Get Summary of Project + Plan [+ build + platform]
        :param project_id:
        :param plan_id:
        :param build_id:
        :param platform_id:
        :param req_id:
        :param report:
        :return:
        """
        executed_summary = {
            'total': 0,
            'executed': 0,
            'executed_rate': 0,
            'pass': 0,
            'pass_rate': 0,
            'pass_total_rate': 0,
            'fail': 0,
            'fail_rate': 0,
            'fail_total_rate': 0,
            'block': 0,
            'block_rate': 0,
            'block_total_rate': 0,
            'notrun': 0,
            'notrun_rate': 0,
            'case': dict(),
            'issue_tracker_uri': self.issue_tracker_uri_view,
            'requirement': dict(),
        }
        if report != '1':
            return executed_summary
        if project_id and plan_id:
            try:
                executed_results = list()
                requirements = self.list_requirement(project_id, plan_id)
                cases = self.testlink.get_plan(project_id=project_id,
                                               plan_id=plan_id,
                                               build_id=build_id,
                                               platform_id=platform_id,
                                               requirement_doc_id=requirements.get(req_id) if req_id else '')
                for case_id, case_info in cases.items():
                    executed_results.append(case_info.get('exec_status'))

                executed_summary['notrun'] = executed_results.count('n')
                executed_summary['pass'] = executed_results.count('p')
                executed_summary['fail'] = executed_results.count('f')
                executed_summary['block'] = executed_results.count('b')
                executed_summary['case'] = cases
                executed_summary['issue_tracker_uri'] = self.issue_tracker_uri_view
                executed_summary['requirement'] = requirements

                executed_summary['total'] = len(executed_results)
                executed_summary['pass_total_rate'] = '%.2f' % float(executed_summary['pass'] / executed_summary['total'] * 100) if executed_summary['total'] != 0 else 0
                executed_summary['fail_total_rate'] = '%.2f' % float(executed_summary['fail'] / executed_summary['total'] * 100) if executed_summary['total'] != 0 else 0
                executed_summary['block_total_rate'] = '%.2f' % float(executed_summary['block'] / executed_summary['total'] * 100) if executed_summary['total'] != 0 else 0
                executed_summary['notrun_rate'] = '%.2f' % float(executed_summary['notrun'] / executed_summary['total'] * 100) if executed_summary['total'] != 0 else 0

                executed_summary['executed'] = sum([executed_summary['pass'],
                                                    executed_summary['fail'],
                                                    executed_summary['block']])
                executed_summary['executed_rate'] = '%.2f' % float(executed_summary['executed'] / executed_summary['total'] * 100) if executed_summary['total'] != 0 else 0
                executed_summary['pass_rate'] = '%.2f' % float(executed_summary['pass'] / executed_summary['executed'] * 100) if executed_summary['executed'] != 0 else 0
                executed_summary['fail_rate'] = '%.2f' % float(executed_summary['fail'] / executed_summary['executed'] * 100) if executed_summary['executed'] != 0 else 0
                executed_summary['block_rate'] = '%.2f' % float(executed_summary['block'] / executed_summary['executed'] * 100) if executed_summary['executed'] != 0 else 0
            except Exception as e:
                logging.warning("[ %s %s ] %s" % (__name__, inspect.stack()[0][3], e))
        return executed_summary


if __name__ == '__main__':
    print('This TMR Client')

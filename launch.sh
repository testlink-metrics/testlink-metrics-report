#!/bin/sh
if [[ -z "${TESTLINK_URL}" ]]; then
    export TESTLINK_URL=''
fi
if [[ -z "${TESTLINK_USER}" ]]; then
    export TESTLINK_USER=''
fi
if [[ -z "${TESTLINK_DEVKEY}" ]]; then
    export TESTLINK_DEVKEY=''
fi
if [[ -z "${ISSUE_TRACKER_URI_VIEW}" ]]; then
    export ISSUE_TRACKER_URI_VIEW=''
fi
export PYTHONPATH=$PWD
python3 metrics/run.py

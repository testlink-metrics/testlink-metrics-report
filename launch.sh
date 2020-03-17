#!/bin/sh
if [[ -z "${TESTLINK_URL}" ]]; then
    echo "Need provide TESTLINK_URL"
    exit 1
fi
if [[ -z "${TESTLINK_USER}" ]]; then
    echo "Need provide TESTLINK_USER"
    exit 1
    export TESTLINK_USER=''
fi
if [[ -z "${TESTLINK_DEVKEY}" ]]; then
    echo "Need provide TESTLINK_DEVKEY"
    exit 1
fi
if [[ -z "${ISSUE_TRACKER_URI_VIEW}" ]]; then
    echo "Need provide ISSUE_TRACKER_URI_VIEW"
    exit 1
fi
export PYTHONPATH=$PWD
python3 metrics/run.py

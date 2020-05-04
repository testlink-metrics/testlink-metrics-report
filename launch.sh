#!/bin/sh
if [[ -z "${TESTLINK_URL}" ]]; then
    echo "TESTLINK_URL is required"
    exit 1
fi
if [[ -z "${TESTLINK_USER}" ]]; then
    echo "TESTLINK_USER is required"
    exit 1
fi
if [[ -z "${TESTLINK_DEVKEY}" ]]; then
    echo "TESTLINK_DEVKEY is required"
    exit 1
fi
if [[ -z "${ISSUE_TRACKER_URI_VIEW}" ]]; then
    echo "ISSUE_TRACKER_URI_VIEW is optional"
fi
export PYTHONPATH=$PWD
python3 metrics/run.py

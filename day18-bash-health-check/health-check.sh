#!/bin/bash

APP_NAME="Node.js Application"
URL="http://localhost:8080/health"
LOG_FILE="$(dirname "$0")/health-check-log.txt"

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "================================="
echo "Application: $APP_NAME"
echo "Check time: $TIMESTAMP"
echo "Checking URL: $URL"
echo "================================="

HTTP_STATUS=$(curl --connect-timeout 3 --max-time 5 -s -o /dev/null -w "%{http_code}" "$URL")
CURL_EXIT=$?

if [ "$CURL_EXIT" -eq 0 ] && [ "$HTTP_STATUS" -eq 200 ]; then
    RESULT="HEALTHY - HTTP $HTTP_STATUS"
    EXIT_CODE=0
else
    RESULT="UNHEALTHY - HTTP $HTTP_STATUS (curl exit: $CURL_EXIT)"
    EXIT_CODE=1
fi

echo "$RESULT"
echo "[$TIMESTAMP] $RESULT" >> "$LOG_FILE"

exit "$EXIT_CODE"

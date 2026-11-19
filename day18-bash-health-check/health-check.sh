#!/bin/bash

APP_NAME="Node.js Application"
URL="http://localhost:8080/health"

echo "================================="
echo "Application: $APP_NAME"
echo "Check time: $(date '+%Y-%m-%d %H:%M:%S')"
echo "Checking URL: $URL"
echo "================================="

HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

if [ "$HTTP_STATUS" -eq 200 ]; then
    echo "HEALTHY - HTTP $HTTP_STATUS"
    exit 0
else
    echo "UNHEALTHY - HTTP $HTTP_STATUS"
    exit 1
fi

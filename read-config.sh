#!/usr/bin/env bash
set -a
source "$(dirname "$0")/.env"
set +a

printf 'Application: %s\n' "$APP_NAME"
printf 'Environment: %s\n' "$APP_ENV"
printf 'Port: %s\n' "$APP_PORT"

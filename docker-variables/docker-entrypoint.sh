#!/bin/sh

# Substitute environment variables in nginx config template
envsubst '$CUSTOM_HEADER' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf

# Start Nginx
exec "$@"

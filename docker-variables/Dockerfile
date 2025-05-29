# Use official nginx image as base
FROM nginx:alpine

# Install envsubst tool to substitute env vars in config
RUN apk add --no-cache gettext

# Copy template config file
COPY default.conf.template /etc/nginx/templates/default.conf.template

# Copy static html
COPY index.html /usr/share/nginx/html/index.html

# Entrypoint script to substitute env vars in config and start nginx
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

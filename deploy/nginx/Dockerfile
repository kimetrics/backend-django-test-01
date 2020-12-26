FROM nginx:stable-alpine

COPY pos-app.conf /etc/nginx/templates/pos-app.conf.template

COPY staticfiles /app/pos/staticfiles/

RUN rm /etc/nginx/conf.d/default.conf

EXPOSE 80
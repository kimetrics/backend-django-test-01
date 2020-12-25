FROM nginx:stable-alpine

COPY pos-app.conf /etc/nginx/conf.d/pos-app.conf

COPY staticfiles /app/pos/staticfiles/

RUN rm /etc/nginx/conf.d/default.conf
EXPOSE 80
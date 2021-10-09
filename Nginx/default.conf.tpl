server {
    listen ${LISTEN_PORT};

    location /static {
        alias /vol/static;
    }

    location /api {
        uwsgi_pass              ${DJANGO_HOST}:${DJANGO_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    15M;
    }
}

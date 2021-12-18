# OctoPrint Assistant

A rest API server designed for vocal control 3d printer with OctoPrint. that fetch data from and issue command to octoprint server, and reply with human understandable language.

Designed be used with together with Siri or Google Assistant.

You can use your voice to get the status and printing time of your 3D printer, and control it by issuing commands like,

1. Get Job Status
1. Start Job
1. Toggle Job
1. Cancel Job
1. etc

## How it's done

See [idea.md](./idea.md) for how the project is designed and created.

## Usage

- Clone the repo
- Create and fill in `.env` file following `.env.template`
- Start dev server with `python manage.py runserver 0.0.0.0:8080`
- See [Deployment Section](#deployment) for deployment instructions

## API Documentation

See https://documenter.getpostman.com/view/6372229/UVJbJyBi

### Notes:

- Running the API provided here won't give you any response, you have to have a server running OctoPrint Assistant so you can test
- A `x-api-key` must be included in the header.
- The domain used in API documentation is `octoprint.local`, you should change it to the domain/ip of your server running OctoPrint Assistant.
- Don't forget to add/update port after the domain/ip.

## Docker Image

https://hub.docker.com/repository/docker/huakunshen/octoprint-assistant

### Build with Dockerfile

```bash
docker build . -t huakunshen/octoprint-assistant
```

**Shortcut**: `make build`

### Build Multi-Platform Docker Image

```bash
docker buildx build \
    --platform linux/amd64,linux/ppc64le,linux/s390x,linux/386,linux/arm/v7,linux/arm/v6,linux/arm64/v8 \
    --push \
    -t huakunshen/octoprint-assistant:latest .
```

**Shortcut**: `make buildx`

## Deployment

You may deploy OctoPrint Assistant using docker. I proposed 2 methods, depending on whether you need a reverse proxy.

- Docker Compose: comes with a nginx reverse proxy ready for SSL setup.

### Docker Compose

The simpliest method is to deploy with `docker-compose`.

```bash
docker-compose up -d
```

This will start 2 services:

- nginx reverse proxy
- OctoPrint Assistant Server

This method is helpful if you don't want to set up a reverse proxy by yourself. Reverse proxy is useful if you plan to expose the OctoPrint Assistant service to public internet and set up SSL certificate for https protocol.

To set up SSL certificate, see [this section](#ssl-certificate).

### Docker Container

The previous method (docker compose) is built upon a docker image [huakunshen/octoprint-assistant](https://hub.docker.com/repository/docker/huakunshen/octoprint-assistant).

If you just need the

```bash
docker run --rm -it -p 8080:8000 \
    -e OCTOPRINT_X_API_KEY=<octoprint-x-api-key> \
    -e OCTOPRINT_ADDRESS=<server-address> \
    -e API_KEY=<api-key> \
    huakunshen/octoprint-assistant
```

```bash
# If you filled in the .env file
docker run --rm -d -p 7000:8000 \
    --name octoprint-assistant \
    --env-file .env \
    huakunshen/octoprint-assistant
```

# SSL Certificate

I use certbot (letsencrypt) to set up SSL certificate.

If you setup reverse proxy by your self, you need to install certbot and enter the following command.

```bash
# change domain.com to yours
certbot certonly -a manual -d <domain.com> --preferred-challenges dns
```

If you are using my `docker-compose.yml` setup, certbot is preinstalled in the nginx proxy. You will need to enter the nginx container first with the container name (should be `octoprint-assitant-reverse-proxy-1`).

```bash
    docker exec -it octoprint-assitant-reverse-proxy-1 bash
```

Then enter the certbox command.

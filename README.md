# OctoPrint Assistant

A rest API server that fetch data from and issue command to octoprint server, and reply with human understandable language.

Designed be used with together with Siri or Google Assistant.

You can use your voice to get the status and printing time of your 3D printer, and control it by issuing commands like,

1. start job
2. toggle job
3. cancel job

## Usage

- Create and fill in `.env` file following `.env.template`
- Start dev server with `python manage.py runserver 0.0.0.0:8080`

## API

- `/octoprint-assistant/printer/state`
- `/octoprint-assistant/job/status`
- `/octoprint-assistant/job/cancel`
- `/octoprint-assistant/job/toggle`
- `/octoprint-assistant/job/start`
- `/octoprint-assistant/connect`
- `/octoprint-assistant/disconnect`
- `/octoprint-assistant/files/all`
- `/octoprint-assistant/files/select`
- `/octoprint-assistant/files/shift`

The `x-api-key` must be included in the header.

## Deployment

The simpliest method is to deploy with `docker-compose`.

```bash
docker-compose up -d
```

# Docker Image

## Build with Dockerfile

```bash
docker build . -t huakunshen/octoprint-assistant
```

## Build Multi-Platform Docker Image

```bash
docker buildx build \
    --platform linux/amd64,linux/ppc64le,linux/s390x,linux/386,linux/arm/v7,linux/arm/v6 \
    --push \
    -t huakunshen/octoprint-assistant:latest .
```

## Run Docker Container

```bash
docker run --rm -it -p 8080:8000 \
    -e OCTOPRINT_X_API_KEY=<octoprint-x-api-key> \
    -e OCTOPRINT_ADDRESS=<server-address> \
    -e API_KEY=<api-key> \
    huakunshen/octoprint-assistant
```

```bash
# if you fill in a .env file
docker run --rm -it -p 8080:8000 \
    --env-file .env \
    huakunshen/octoprint-assistant
```

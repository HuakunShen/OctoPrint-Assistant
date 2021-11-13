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

- `/octoprint-assistant/printer/state/`
- `/octoprint-assistant/job/status/`
- `/octoprint-assistant/job/cancel/`
- `/octoprint-assistant/job/toggle/`
- `/octoprint-assistant/job/start/`

The `x-api-key` must be included in the header.

## Deployment

The simpliest method is to deploy with `docker-compose`.

```bash
docker-compose up -d
```
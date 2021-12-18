# Idea

## Motivation

[OctoPrint](https://octoprint.org/) is a web interface for your 3D printer that allows you to control and monitor all aspects of your printer and print jobs. Users can easily control their 3D printers remotely within a browser.

I have set up a VPN server at home and port forwarding on my router and modem to allow me to monitor and control my printer from outside of my home.

Then I came up with the idea of voice-control my 3D printer.

## OctoPrint Rest API

Once I found that OctoPrint provides [Rest API](https://docs.octoprint.org/en/master/api/index.html), I know it's super easy to achieve voice control.

Rest API allows my to control 3D printers and retrieve information from it with http requests. I could control 3D printer through OctoPrint by sending web request with Siri (given that port forwarding is set up in your router). The reponse from the rest API is in json format, so it's not possible to know whether my commands are successful with siri.

## OctoPrint Assistant

I wrote this OctoPrint Assistant Django server to translate OctoPrint's response to human understandable language.

For example, when you ask Siri, **"What's the printing time left?"**. Siri will send a request to OctoPrint Asssistant, OctoPrint Assistant will send a request to OctoPrint server to get the status of current job. Once OctoPrint Assistant gets the response from OctoPrint server, it will parse the required information and reply to Siri in a human-understandable language, such as, **"Dear Master, the printing time left is 1 hour and 30 minutes."**.

## Router Configuration

Implementing and deploying the Django server is simple, but in order for Siri to work from outside home, you will need to set up port forwarding on your router.

## SSL Certificate (HTTPS)

In addition, since the requests sent with Siri is exposed to public internet, using HTTP protocol is extremely dangerous. Although an API key is required to access OctoPrint Assistant, HTTP protocol doesn't encrypt the API key in request header. Someone with knowledge could easily get your API key and control your 3D printer.

HTTPS must be set up to encrypt your traffic (API key). In this project, nginx is used as a reverse proxy and to set up SSL certificate. You can of course set up SSL certificate directly on Django, but since I have multiple services like this, I prefer to use nginx which can set up everything together.

Certbot is used to generate SSL certificate with letsencrypt.

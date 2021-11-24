buildx:
	docker buildx build \
		--platform linux/amd64,linux/ppc64le,linux/s390x,linux/386,linux/arm/v7,linux/arm/v6 \
		--push \
		-t huakunshen/octoprint-assistant:latest .
build:
	docker build -t huakunshen/octoprint-assistant:latest .

run:
	docker pull huakunshen/octoprint-assistant
	docker run --rm -d -p 7000:8000 \
		--name octoprint-assistant \
		--env-file .env \
		huakunshen/octoprint-assistant

update:
	docker stop octoprint-assistant
	docker rm octoprint-assistant
	docker pull huakunshen/octoprint-assistant
	docker run --rm -d -p 7000:8000 \
		--name octoprint-assistant \
		--env-file .env \
		huakunshen/octoprint-assistant
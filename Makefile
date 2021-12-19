deploy:
	bash ./scripts/update.sh

update:
	bash ./scripts/update.sh

stop:
	bash ./scripts/stop.sh

buildx:
	docker buildx build \
		--platform linux/amd64,linux/ppc64le,linux/s390x,linux/386,linux/arm/v7,linux/arm/v6,linux/arm64/v8 \
		--push \
		-t huakunshen/octoprint-assistant:latest .
build:
	docker build -t huakunshen/octoprint-assistant:latest .

reset-and-backup:
	cp ./config/default ./config/default.bk
	git reset --hard
	git pull
	cp ./config/default.bk ./config/default
	rm ./config/default.bk

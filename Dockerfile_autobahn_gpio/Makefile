.PHONY: build

build:
	sudo docker build -t dockertest .

run:
	sudo docker run --name jerry --device /dev/mem:/dev/mem --privileged dockertest

list:
	sudo docker images

remove_all:
	sudo docker rmi dockertest	

stop:
	sudo docker stop jerry

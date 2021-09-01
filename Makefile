build:
	docker-compose build

build-deploy:
	docker-compose -f docker-compose-deploy.yml build
	
run:
	docker-compose up --build

run-deploy:
	docker-compose -f docker-compose-deploy.yml up --build

up:
	docker-compose up
	
up-deploy:
	docker-compose -f docker-compose-deploy.yml up

down:
	docker-compose -f docker-compose-deploy.yml down
	docker-compose down

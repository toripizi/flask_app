build:
	docker build -t ctf/task_1:latest .

start:
	docker-compose up --detach

stop:
	docker-compose down

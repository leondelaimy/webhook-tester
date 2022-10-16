test: 
		flake8 && \
		pytest

up: 
		docker-compose up

down: 
		docker-compose down

process_queue: 
		rq worker		

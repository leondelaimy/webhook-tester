test: 
		flake8 && \
		pytest

up: 
		docker-compose build && \
		docker-compose up
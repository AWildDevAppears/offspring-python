shell:
	poetry shell

run: run_fe run_be

run_fe:
	cd ./frontend/ && npm run dev

run_be:
	poetry run python offspringengine

lint:
	poetry run yapf -i --recursive offspringengine

fixtures:
	poetry run python offspringengine/fixtures.py

dll:
	go build -buildmode=c-shared -o datastore.so ./offsprung/datastore.go

build-pkl:
	pkl eval data/combateers.pkl -o database.json -f json

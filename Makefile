test:
	cd ./FindBlaBlaCarBot/ && python3 test.py
	cd ./FindBlaBlaCarBot/ && coverage test.py
	cd ./FindBlaBlaCarBot/ && codecov

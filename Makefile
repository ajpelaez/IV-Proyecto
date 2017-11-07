test:
	cd ./FindBlaBlaCarBot/ && coverage run test.py
coverage:
	cd ./FindBlaBlaCarBot/ && codecov

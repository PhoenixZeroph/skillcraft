.PHONY: demo test lint sbom

demo:
	uvicorn app.main:api --reload &\
	streamlit run streamlit_app/Home.py

test:
	pytest -n auto --cov

lint:
	pylint app agents streamlit_app

sbom:
	cyclonedx-py -o sbom.xml
venv:
	python3 -m venv ics-env
setenv:
	source ics-env/bin/activate
api-lib:
	pip3 install fastapi uvicorn urlopen
model-lib:
	pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
service:
	uvicorn main:app --host 0.0.0.0 --port 8000
# Service for generating genres from book cover images

## Running native

### Running first time

Download model from drive into model folder
Run all command in Makefile

### Restart service

Run `make service`

### API documents

For document access http://0.0.0.0:8000/docs

## Running with docker

### Running first time

Download model from drive into model folder
Rename to `model_v3.pt`

#### Build image

Run `make build` if you have make or you can copy command in Makefile

#### Run container

Run `make run` if you have make or you can copy command in Makefile

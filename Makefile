

.PHONY: help run

help:
	@echo "  run               - Run FastAPI application locally"

run:
	fastapi dev app/main.py
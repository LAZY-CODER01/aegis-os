.PHONY: help run-backend run-desktop test lint install

# Dynamically resolve root directory
ROOT_DIR := $(CURDIR)
VENV := $(ROOT_DIR)/.venv/bin

help:
	@echo "Available commands:"
	@echo "  make run-backend  - Start FastAPI backend server"
	@echo "  make run-desktop  - Start Vite desktop frontend"
	@echo "  make test         - Run backend and desktop tests"
	@echo "  make lint         - Run linters across projects"
	@echo "  make install      - Install all dependencies"

# --- Backend Commands ---
backend:
	cd apps/backend && $(VENV)/uvicorn app.main:app --reload

test-backend:
	cd apps/backend && $(VENV)/pytest

lint-backend:
	cd apps/backend && $(VENV)/ruff check .

# --- Desktop Frontend Commands ---
frontend:
	cd apps/desktop && npm run dev

test-desktop:
	cd apps/desktop && npm run test

lint-desktop:
	cd apps/desktop && npm run lint

# --- Combined Targets ---
test: test-backend test-desktop
lint: lint-backend lint-desktop

install:
	python3 -m venv .venv
	$(VENV)/pip install -r apps/backend/requirements.txt
	cd apps/desktop && npm install
# Used by `test-api` target
TEST_HOST ?= localhost:5000

# Don't change
SRC_DIR := 

.PHONY: help lint lint-fix image push run deploy undeploy clean test-api .EXPORT_ALL_VARIABLES
.DEFAULT_GOAL := help

help:  ## 💬 This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

run: venv  ## 🏃 Run the server locally using Python & Flask
	. $(SRC_DIR)/.venv/bin/activate \
	&& python backend/main.py

test: venv  ## 🎯 Unit tests for Flask app
	. $(SRC_DIR)/.venv/bin/activate \
	&& pytest -v

# ============================================================================

venv: $(SRC_DIR)/.venv/touchfile

$(SRC_DIR)/.venv/touchfile: $(SRC_DIR)/backend/requirements.txt
	python3 -m venv $(SRC_DIR)/.venv
	. $(SRC_DIR)/.venv/bin/activate; pip install -Ur $(SRC_DIR)/requirements.txt
	touch $(SRC_DIR)/.venv/touchfile

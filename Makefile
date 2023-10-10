.PHONY: lint
lint: 
	@echo "--- Running black"
	@black .

	@echo "--- Running ruff"
	@ruff check . --fix
	
	@echo "--- Running mypy"
	@mypy .

.PHONY: lint
lint: 
	@echo "--- Running black"
	@black .

	@echo "--- Running ruff"
	@ruff check . --fix
	
	@echo "--- Running mypy"
	@mypy .

.PHONY: build
build:
	@docker build -t mawlle/maxgram .

.PHONY: push
push:
	@docker push mawlle/maxgram
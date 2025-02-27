install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reassemble:
	uv tool install --force dist/*.whl

check-lint:
	uv run ruff check brain_games

fix-lint:
	uv run ruff check --fix brain_games

build:
	python3 -m build

deploy:
	twine check dist/*
	twine upload dist/*

clean:
	rm -rf src/*.egg-info
	rm -rf dist/

rebuild: clean build

install_build_dependencies:
	python3 -m pip install --upgrade build twine

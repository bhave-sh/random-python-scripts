$(which python3) -m pip install pipenv
pipenv --three sync
# pipenv shell
pipenv run python3 scrape_crs_score.py

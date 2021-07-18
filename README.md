# Home Automation API

Server to run on raspberry pi for home automation

### Setting up the project
1. Create a virtual env in folder `python3 -m venv home-api`
1. Activate the virtual env with:
	- `source bin/activate` Unix
	- `Scripts\activate.bat` Windows
1. Install dependencies `python -m pip install -r requirements.txt`

### Running the server 
1. Execute `flask run` to start the dev server

#### Updating dependencies
Install dependency to venv and execute `python -m pip freeze > requirements.txt` to update requirements.txt
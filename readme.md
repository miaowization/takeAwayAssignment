# Setup project
1. Clone the repository and go to the project folder.

2. Install requirements
`pip install -U -r requirements.txt`
3. Get a chromedriver and write its location to PATH

4. Install allure. If you have Mac OS X and you have Homebrew just execute command in terminal
` brew install allure`. 
Or else see installation steps in documentation https://docs.qameta.io/allure/#_get_started

5. To run tests execute command `pytest --alluredir=tmp/my_allure_results`.
That will run all the tests and create a test report.

6. To open HTML test report execute command `allure serve tmp/my_allure_results` 
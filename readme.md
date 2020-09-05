# Setup project

There are 2 ways how you can get run the tests: locally on your computer or 
in Azure Devops pipeline which I created to relieve you from setting up 
the environment needed to run tests.

###### If you want to do it wasy way:
1. Open the link 
https://gabidulina.visualstudio.com/takeAwayQAAssignment/_build?definitionId=1 
in your browser. There you will find a pipeline with these steps 

![pipeline steps](resources/pipeline_steps.jpg =250x) 

###### If you want to do it the hard way follow instruction:
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


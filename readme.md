# Setup project

There are 2 ways how you can get run the tests: locally on your computer or 
in Azure Devops pipeline which I created to relieve you from setting up 
the environment needed to run tests.

###### If you want to do it easy way:
1. Open the link 
https://gabidulina.visualstudio.com/takeAwayQAAssignment/_build?definitionId=1 
in your browser. There you will find a pipeline with these steps:
- Checkout repository
- Install Google Chrome
- Install Allure
- Install Firefox
- Install python requirements
- Run tests with Pytest in headless browser, by default Firefox
- Generate test report with Allure
- Send test report to Github Pages

Unfortunately the pipeline can be started only if you have permission to start it. 
So if you want to do it yourself please contact me in Telegram @AigulValieva 
or by e-mail aigul.g.r@gmail.com.

Otherwise you can just open previously runned jobs and look at the results. 
Test report can be found here https://miaowization.github.io/takeAwayAssignment.
Also it is published as pipeline artifact.
![pipeline artifact](resources/pipeline_artifact.png) 

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


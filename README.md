# PythonTestAutomation

Install packages after coming to the root directory:

pip install -r requirements.txt

Create new virtual environment :
python -m venv env_name 

Activate the created environment:

env_name\Scripts\activate.bat

source env_name/bin/activate(mac & linux)

Running test from cmd:

Pytest normal:        

py.test (runs all test scripts)

py.test tests/file_name.py (runs all test scripts which are contained in file file_name.py under tests directory)

py.test -m smoke (runs test scripts containing "smoke" mark

py.test --browser_name="firefox" (runs all test scripts in firefox, default is chrome)

py.test --html=reports/xyz.html (runs all test scripts and generates html report in reports folder with filename 'xyz.html')
 
Sample command using all flags:  py.test -m end_to_end --browser_name="firefox" --html=reports/end_to_end.html
    
BDD: There are two feature files (search.feature, end_to_end.feature. Run using cmd by:
behave features/feature_file_name.feature

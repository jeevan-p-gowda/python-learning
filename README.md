PyTest commands to execute tests

Go to project directory

#To run all tests with verbose and console output
py.test -v -s

#To run tests of particular python file
py.test filename.py -v -s

#To run test for particular methods using its name
py.test -k methodname -v -s

#To run test for marked methods using given name (Ex:- Smoke, Regression)
py.test -m givename -v -s

Generating report 
pytest --html=report.html

(If causes any error then execute:- pip3 install pytest-html)

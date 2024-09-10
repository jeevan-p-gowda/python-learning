Python Learning <img align="right" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg">
=
This repo has my learning on Python which encompasses following topics, essential for building an test framework.

```shell
pip install -r requirements.txt
```

Concepts
-
OOP's, File Handling - Context Managers, Exception Handling, Collections, Programs & Tips & Tricks.

PyTest Framework <img align="right" src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg" width="100">
-
Path - `./Pytest`

PyTest `commands` to execute tests :-

1.To run all tests with verbose and console output
```shell
py.test -v -s
```
2.To run tests of particular python file
```shell
py.test filename.py -v -s
```
3.To run test for particular methods using its name
```shell
py.test -k methodname -v -s
```
4.To run test for marked methods using given name (Ex:- Smoke, Regression)
```shell
py.test -m givename -v -s
```
5.Generating report 
```shell
pytest --html=report.html
```
>If any error then execute:- 
> ```shell
> pip3 install pytest-html
> ```
>

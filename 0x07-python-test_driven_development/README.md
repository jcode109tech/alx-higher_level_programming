0X07-python-test_driven_developmet

--------------------------------------------
All your tests should be executed by using this command:

python3 -m doctest ./tests/*

--------------------------------------------
All your modules should have a documentation 

python3 -c 'print(__import__("my_module").__doc__)'

example:

python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)'

python3 -c 'print(__import__("0-main").__doc__)'

----------------------------------------------
All your functions should have a documentation 

(python3 -c 'print(__import__("my_module").my_function.__doc__)')

example:
python3 -c 'print(__import__("0-main.my_module").__doc__)'
import importlib.machinery
import pso_test
import sys
from inspect import getmembers, isfunction

def line():
  print(u'\u2500' * 50)

name = sys.argv[1]
module = importlib.machinery.SourceFileLoader("name", './{}.py'.format(name)).load_module()
functions = getmembers(module, isfunction)
total_tests = 0
passed = 0

for name, test in functions:

  if name[0:4] == "test":
    total_tests += 1
    result = test()
    if result == True:
      passed += 1
    else: 
      line()
      print(name)
      print(result)
      line()


line()
print("Passed {} out of {} tests!".format(passed, total_tests))
line()



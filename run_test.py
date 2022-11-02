import importlib.machinery
import os
import sys
from inspect import getmembers, isfunction

def line():
  print(u'\u2500' * 50)

file = sys.argv[1]
name = os.path.splitext(file)[0]

while True:
  print(name, file)
  try:
    module = importlib.machinery.SourceFileLoader(name, './{}'.format(file)).load_module()
    break

  except:
    print("file not found.")
    file = input("Please re-enter file or type EXIT!: ")
    if file == "EXIT!":
      break

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



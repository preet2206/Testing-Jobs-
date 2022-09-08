import os

os.environ["NBOX_LOG_LEVEL"] = "INFO"

import sys
from nbox import operator, Operator, RelicsNBX, Job
from nbox.operator import Resource

@operator()
def test():
  print("Cheers! Your new nbox version is working")

@operator()
def square(i = 5):
  return i * i
  
if __name__ == "__main__":
  test = test()
  square = square()
  

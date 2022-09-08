from nbox import operator, Operator

@operator()
class Squared:
  def __init__(self, num: float = 8.0):
    self.num = num
  
  def sqaured(self):
    square = self.num ** 2
    return square

if __name__ == "__main__":
  sqaure = Squared()
  print("[local]", square)
  print("[local]", Squared.num)
  print("[local]", sqaure.sqaured())

  square_deploy = square.deploy(
    "wnja9glc",
    id_or_name = "ycfymwun",
    deployment_type = "serving",
  )
  print("[square_deploy]", square)
  print("[square_deploy]", Squared.num)
  print("[square_deploy]", sqaure.sqaured())

  op = Operator.from_serving(
    "https://api.nimblebox.ai/ycfymwun/",
    "nbxdeploy_zwgcBwducL0OCPxFMWrC4P8dExTqlZMBZ8HA2TSX",
  )

  print(op)

  print(op.num)
  print(op.squared())
  

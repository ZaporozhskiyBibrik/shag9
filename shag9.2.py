import random
def error_logger(func):
  def wrapper(*args, **kwargs):
      try:
          return func(*args, **kwargs)
      except Exception as e:
          print(f"An error occurred: {e}")
          return None
  return wrapper
@error_logger
def calculator(a, b, operation):
  if operation == '+':
      return a + b
  elif operation == '-':
      return a - b
  elif operation == '*':
      return a * b
  elif operation == '/':
      return a / b
  else:
      raise ValueError("Invalid operation")
result = calculator(10, 0, '/')
print(result)

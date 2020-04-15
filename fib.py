def fib(n):
  # base case
  if n <= 2:
    return 1
  # recursive call, should move toward base case
  return fib(n-1) + fib(n-2)
fib(10)
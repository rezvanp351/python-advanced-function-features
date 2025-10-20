# -------------------------------
# Python Advanced Topics
# Topics: *args/**kwargs, Scope, Decorators, Lambda, Recursion, Generators
# Each example includes comments explaining the behavior for beginners.
# -------------------------------

# 1) *args and **kwargs
# ---------------------
# *args collects extra positional arguments as a tuple.
# def show_args(*args):
#     # args is a tuple of all additional positional values
#     print("args (tuple):", args)
#     for i, val in enumerate(args, 1):
#         print(f"  arg {i} ->", val)

# show_args(10, 20, "hello")


# **kwargs collects extra keyword arguments as a dict.
# def show_kwargs(**kwargs):
#     # kwargs is a dict mapping parameter name -> value
#     print("\nkwargs (dict):", kwargs)
#     for k, v in kwargs.items():
#         print(f"  {k} -> {v}")

# show_kwargs(name="Aref", age=25, country="Afghanistan")


# Mix positional, *args, and **kwargs
# def mixed(a, b, *args, **kwargs):
#     print(f"\nRequired a={a}, b={b}")
#     print("Additional args:", args)
#     print("Keyword args:", kwargs)

# mixed(1, 2, 3, 4, x=10, y=20)


# 2) Python Scope (local, global, nonlocal)
# ----------------------------------------
# Local variables exist inside functions.
# def local_example():
#     x = "local x"
#     print("\nInside local_example:", x)

# local_example()
# print(x)  # Would raise NameError because x is not defined here

# Global variables: declared at module level
# g = "global g"

# def read_global():
#     # reading global variable is allowed without 'global' keyword
#     print("Read global g:", g)

# read_global()

# def modify_global():
#     global g  # declare intent to use the global variable for assignment
#     g = "modified global g"
#     print("Modified global g inside function:", g)

# modify_global()
# print("Global g after modify_global():", g)


# nonlocal: used inside nested functions to modify variable in enclosing scope
# def outer():
#     x = "outer x"
#     def inner():
#         nonlocal x
#         x = "changed by inner"
#         print("Inner changed x to:", x)
#     inner()
#     print("Outer sees x as:", x)

# print()
# outer()


# 3) Python Decorators
# --------------------
# Decorators wrap a function to extend its behavior without changing the function code.
# from functools import wraps
# def simple_decorator(func):
#     @wraps(func)  # keeps original function metadata (__name__, __doc__)
#     def wrapper(*args, **kwargs):
#         print("\n[Decorator] Before calling", func.__name__)
#         result = func(*args, **kwargs)
#         print("[Decorator] After calling", func.__name__)
#         return result
#     return wrapper

# @simple_decorator
# def say(message):
#     """Say something simple"""
#     print("say():", message)
#     return "done"

# ret = say("Hello Decorator")
# print("Decorator returned:", ret)
# print("say.__name__:", say.__name__)
# print("say.__doc__:", say.__doc__)

# # Decorator with arguments: use an outer function returning a decorator
# def repeat(times):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(times):
#                 print(f"[repeat] Call {i+1} of {times}")
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def hello(name):
#     print("Hello", name)

# hello("Aref")


# 4) Lambda (anonymous) functions
# -------------------------------
# A lambda is a short anonymous function expression: lambda args: expression
# add = lambda x, y: x + y
# print("\nLambda add(3,5):", add(3, 5))

# # Useful with map, filter and sorted
# nums = [5, 2, 9, 1, 7]
# squared = list(map(lambda n: n*n, nums))
# evens = list(filter(lambda n: n % 2 == 0, nums))
# sorted_desc = sorted(nums, key=lambda n: -n)
# print("squared:", squared)
# print("evens:", evens)
# print("sorted_desc:", sorted_desc)

# Lambda for short one-line functions; avoid complex logic in lambda for readability


# 5) Recursion
# ------------
# A function that calls itself. Example: factorial
# def factorial(n):
#     """Return n! (factorial) using recursion"""
#     if n < 0:
#         raise ValueError("Negative values not allowed")
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# print("\nfactorial(5):", factorial(5))

# # Fibonacci using recursion (simple but exponential time)
# def fib(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# print("fib(7):", fib(7))

# Recursion depth warning: Python has a recursion limit (default ~1000)
# Use iterative solutions for deep recursion or increase recursion limit carefully.

# 6) Generators
# -------------
# Generators produce values lazily using 'yield' and are memory-efficient.
# def count_up_to(max_value):
#     count = 1
#     while count <= max_value:
#         yield count  # pause and yield a value to the caller
#         count += 1

# print("\nGenerator count_up_to(5):", list(count_up_to(5)))

# # Generator expression (similar to list comprehension but lazy)
# gen_expr = (x*x for x in range(5))
# print("Generator expression next values:")
# print(next(gen_expr))
# print(next(gen_expr))

# Sending values to generator (advanced): generator can receive data with .send()
# def grep(pattern):
#     print("\n[gain] Starting grep generator for pattern:", pattern)
#     try:
#         while True:
#             line = (yield)  # receive a line sent by caller
#             if pattern in line:
#                 print("Found:", line)
#     except GeneratorExit:
#         print("Generator closed")

# g = grep("hello")
# next(g)          # prime the generator (advance to first yield)
# g.send("no match here")
# g.send("this has hello inside")
# g.close()        # close the generator

# # Summary examples
# if __name__ == "__main__":
#     print("\n-- Summary Example Calls --")
#     show_args(1,2,3)
#     show_kwargs(a=1,b=2)
#     print("factorial(6):", factorial(6))

# Python Advanced Topics

This tutorial demonstrates **advanced Python concepts** including `*args`, `**kwargs`, scopes, decorators, lambda functions, recursion, and generators.  
Each example is **fully commented** to help beginners understand how and why things work.

---

## 🧩 Topics Covered
1. *args and **kwargs
2. Python Scope (local, global, nonlocal)
3. Python Decorators
4. Lambda (anonymous functions)
5. Recursion
6. Generators

---

## 📘 Code with Explanations

```python
# -------------------------------
# Python Advanced Topics
# Topics: *args/**kwargs, Scope, Decorators, Lambda, Recursion, Generators
# Each example includes comments explaining the behavior for beginners.
# -------------------------------

# 1) *args and **kwargs
# ---------------------
def show_args(*args):
    print("args (tuple):", args)
    for i, val in enumerate(args, 1):
        print(f"  arg {i} ->", val)

show_args(10, 20, "hello")


def show_kwargs(**kwargs):
    print("\nkwargs (dict):", kwargs)
    for k, v in kwargs.items():
        print(f"  {k} -> {v}")

show_kwargs(name="Aref", age=25, country="Afghanistan")


def mixed(a, b, *args, **kwargs):
    print(f"\nRequired a={a}, b={b}")
    print("Additional args:", args)
    print("Keyword args:", kwargs)

mixed(1, 2, 3, 4, x=10, y=20)


# 2) Python Scope (local, global, nonlocal)
# ----------------------------------------
def local_example():
    x = "local x"
    print("\nInside local_example:", x)

local_example()

g = "global g"

def read_global():
    print("Read global g:", g)

read_global()

def modify_global():
    global g
    g = "modified global g"
    print("Modified global g inside function:", g)

modify_global()
print("Global g after modify_global():", g)


def outer():
    x = "outer x"
    def inner():
        nonlocal x
        x = "changed by inner"
        print("Inner changed x to:", x)
    inner()
    print("Outer sees x as:", x)

print()
outer()


# 3) Python Decorators
# --------------------
from functools import wraps

def simple_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\n[Decorator] Before calling", func.__name__)
        result = func(*args, **kwargs)
        print("[Decorator] After calling", func.__name__)
        return result
    return wrapper

@simple_decorator
def say(message):
    '''Say something simple'''
    print("say():", message)
    return "done"

ret = say("Hello Decorator")
print("Decorator returned:", ret)
print("say.__name__:", say.__name__)
print("say.__doc__:", say.__doc__)


def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"[repeat] Call {i+1} of {times}")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello(name):
    print("Hello", name)

hello("Aref")


# 4) Lambda (anonymous) functions
# -------------------------------
add = lambda x, y: x + y
print("\nLambda add(3,5):", add(3, 5))

nums = [5, 2, 9, 1, 7]
squared = list(map(lambda n: n*n, nums))
evens = list(filter(lambda n: n % 2 == 0, nums))
sorted_desc = sorted(nums, key=lambda n: -n)
print("squared:", squared)
print("evens:", evens)
print("sorted_desc:", sorted_desc)


# 5) Recursion
# ------------
def factorial(n):
    if n < 0:
        raise ValueError("Negative values not allowed")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print("\nfactorial(5):", factorial(5))

def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print("fib(7):", fib(7))


# 6) Generators
# -------------
def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1

print("\nGenerator count_up_to(5):", list(count_up_to(5)))

gen_expr = (x*x for x in range(5))
print("Generator expression next values:")
print(next(gen_expr))
print(next(gen_expr))

def grep(pattern):
    print("\n[gain] Starting grep generator for pattern:", pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print("Found:", line)
    except GeneratorExit:
        print("Generator closed")

g = grep("hello")
next(g)
g.send("no match here")
g.send("this has hello inside")
g.close()

if __name__ == "__main__":
    print("\n-- Summary Example Calls --")
    show_args(1,2,3)
    show_kwargs(a=1,b=2)
    print("factorial(6):", factorial(6))
```

---

## 💡 Notes
- Use this file as a **learning script** by running it line-by-line.
- Best for **intermediate Python learners** improving functional and conceptual understanding.

---

Made with ❤️ by **Muhammad Aref Rezvan Panah**
---

## 📎 Author
👩‍💻 **Created by: ❤️ by **Muhammad Aref Rezvan Panah**
📅 **Year:** 2025  
💬 **Language:** Python 3.10  
🎯 **Purpose:** Teaching Python functions in a clear and beginner-friendly way.

---

## 💖 Support & Feedback
If this repository helped you, please consider:
- ⭐ **Starring** the repo  
- 🗨️ **Commenting** your thoughts  
- 📢 **Sharing** it with others learning Python  

Your feedback motivates more free educational content!

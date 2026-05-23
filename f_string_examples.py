"""f_string_examples.py — 7 things you can do with f-strings in Python.

Run:
  python f_string_examples.py
"""
from datetime import date

name = "Alice"
price = 1234.5678
count = 42
today = date(2026, 5, 23)

# 1. Basic interpolation — drop a variable into a string
print("=== 1. basic interpolation ===")
print(f"Hello, {name}")
print()

# 2. Format spec — numbers, alignment, percentages
print("=== 2. format spec ===")
print(f"price: ${price:,.2f}")       # 1,234.57 with thousand separator
print(f"count: |{count:>6}|")        # right-pad to width 6
print(f"pct:   {0.1234:.2%}")        # percentage with 2 decimals
print()

# 3. Expressions inside the braces — not just variables
print("=== 3. expressions inside braces ===")
items = [10, 20, 30]
print(f"first: {items[0]}")
print(f"sum:   {sum(items)}")
print(f"upper: {name.upper()}")
print()

# 4. = for debugging (Python 3.8+) — prints both expression and value
print("=== 4. = for debugging ===")
x, y = 10, 20
print(f"{x=}, {y=}, {x+y=}")
print()

# 5. !r / !s / !a conversion flags
print("=== 5. conversion flags ===")
words = ["python", "lambda"]
greet = "café"
print(f"with str:   {words!s}")      # ['python', 'lambda']
print(f"with repr:  {words!r}")      # same, but quoted strings inside
print(f"with ascii: {greet!a}")      # escapes non-ascii: 'caf\xe9'
print()

# 6. Multi-line f-strings — triple quotes
print("=== 6. multi-line ===")
msg = f"""
=== Report ===
name:  {name}
price: ${price:,.2f}
date:  {today}
"""
print(msg.strip())
print()

# 7. Date / time formatting — strftime codes inside the format spec
print("=== 7. date formatting ===")
print(f"iso:  {today:%Y-%m-%d}")
print(f"long: {today:%A, %B %d %Y}")

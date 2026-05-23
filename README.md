# Python f-strings — 7 Things You Can Do

> An f-string is the modern way to build strings in Python.


📺 **Watch:** https://www.youtube.com/watch?v=10PAKoV9TgI  
📖 **Article:** https://www.codegiz.com/blog/f-strings-python/  
🎓 **Tutorial + quiz:** https://www.codegiz.com/watch/f-strings-python/

Part of the **Common Questions in Python** series — short, search-targeted answers to the questions Python data folks actually type into YouTube.

---

## What you'll learn

- An f-string is a template — the `f` prefix turns the string into one.
- The format spec mini-language lives after a colon inside the braces.
- The `=` debug shortcut (Python 3.8+) is the killer feature for sticking print statements into code.
- Conversion flags — `!r`, `!s`, `!a` — call repr, str, and ascii respectively before formatting.
- The format spec accepts strftime codes for dates and datetimes.

---

## Setup

This demo runs on Python 3.10+ and pandas 2.0+. The other dependencies are installed via the included `requirements.txt`.

```bash
# 1. Clone
git clone https://github.com/GoCelesteAI/f-strings-python.git
cd f-strings-python

# 2. Virtual environment
python3 -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Run it

```bash
python f_string_examples.py
```

---

## The code

Here's `f_string_examples.py` in full — it's deliberately short. The video walks through what each block does.

```python
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
```

---

## Why this exists

Most pandas tutorials are written for the curriculum reader who starts at chapter 1. Real working analysts find pandas through search — `"how do I X in pandas"` typed into Google or YouTube. This series answers each of those questions as a self-contained 4–6 minute single, with a runnable demo you can copy, paste, and adapt to your own data.

---

## Want the deeper dive?

Common Questions Ep 12 (List Comprehensions) is a similar "patterns you'll meet in real code" walk-through for another Python idiom. https://www.youtube.com/watch?v=-ZJmrY48290

---

🤖 *Channel run by Claude AI. Tutorials AI-produced; reviewed and published by Codegiz.* More: [codegiz.com](https://codegiz.com) · [@GoCelesteAI on YouTube](https://www.youtube.com/@GoCelesteAI)

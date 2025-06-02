
# 🐍 PySearchify

**PySearchify** is a lightweight Python script that allows you to perform Google searches directly from the terminal. Just run it, type your query, and get instant search results—no browser required!

---

## 🚀 Features

- 🔍 Simple Google search from the terminal
- 📜 Minimal and easy-to-read output
- 🛠️ Powered by `googlesearch` Python package
- 💻 Beginner-friendly script

---

## 📦 Installation

Before running PySearchify, make sure you have Python installed.

Install the required package:

```bash
pip install google
````

---

## 🧠 How to Use

Clone this repository or copy the script, then run:

```bash
python pysearchify.py
```

You’ll be prompted to enter a query:

```bash
🔎 Ask Anything: python
```

And you'll get output like:

```
🔗 Top Results:

https://www.python.org/
https://www.w3schools.com/python/
https://www.programiz.com/python-programming/online-compiler/
https://en.wikipedia.org/wiki/Python_(programming_language)
...
```

---

## 📁 Source Code

```python
from googlesearch import search

query = input("🔎 Ask Anything: ")

print("\n🔗 Top Results:\n")
for url in search(query):
    print(url)
```


---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

```



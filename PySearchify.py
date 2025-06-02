# PySearchify - Search anything using Python!

# Install the necessary package
# pip install google

from googlesearch import search

# Take user input
query = input("🔎 Ask Anything: ")

# Perform Google search and print results
print("\n🔗 Top Results:\n")
for url in search(query):
    print(url)

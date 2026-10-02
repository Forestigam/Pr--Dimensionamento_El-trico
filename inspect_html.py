with open(r"C:\Users\Edimar\.gemini\antigravity\scratch\dimensionamento_eletrico.html", "r", encoding="utf-8") as f:
    content = f.read()

print("Length:", len(content))
print("btnFaseMono in text:", "btnFaseMono" in content)
print("loadCardsContainer in text:", "loadCardsContainer" in content)
print("DOMContentLoaded in text:", "DOMContentLoaded" in content)

# Extract script tag content and test syntax
script_start = content.find("<script>")
script_end = content.rfind("</script>")
script = content[script_start+8:script_end]

with open(r"C:\Users\Edimar\.gemini\antigravity\scratch\test_script.js", "w", encoding="utf-8") as f:
    f.write(script)

print("Script written to test_script.js")

import os

with open(r"C:\Users\Edimar\.gemini\antigravity\scratch\dimensionamento_eletrico.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's inspect where loadCardsContainer is and check how initial load card is rendered.
print("Check loadCardsContainer placement:")
idx = html.find('id="loadCardsContainer"')
print(html[idx-100:idx+200])

print("\nCheck btn-add-load placement:")
idx2 = html.find('btn-add-load')
print(html[idx2-100:idx2+200])

with open(r"C:\Users\Edimar\.gemini\antigravity\scratch\dimensionamento_eletrico.html", "r", encoding="utf-8") as f:
    html = f.read()

start = html.find("function renderizarCardsCargas()")
end = html.find("function atualizarCarga", start)

with open(r"C:\Users\Edimar\.gemini\antigravity\scratch\render_code.txt", "w", encoding="utf-8") as f:
    f.write(html[start:end])

print("Written render_code.txt")

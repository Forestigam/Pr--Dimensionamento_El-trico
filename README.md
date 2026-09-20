# ⚡ Pré-Dimensionamento Elétrico — ABNT NBR 5410

> Ferramenta web gratuita para pré-dimensionamento de circuitos elétricos de baixa tensão, baseada nos critérios da **ABNT NBR 5410:2004**.

🔗 **[Acessar a ferramenta online](https://forestigam.github.io/Pr--Dimensionamento_El-trico/)**

---

## 📋 Sobre o Projeto

Aplicativo web profissional desenvolvido para engenheiros eletricistas, técnicos e estudantes que precisam realizar o **pré-dimensionamento de circuitos elétricos de baixa tensão** de forma rápida e confiável.

O sistema avalia simultaneamente os dois critérios fundamentais da NBR 5410:
- **Capacidade de condução de corrente (Iz ≥ Ib)**
- **Queda de tensão (ΔV% ≤ 4,00%)**

---

## ✨ Funcionalidades

- ⚡ **Cálculo vetorial completo** — potências ativa, reativa e aparente por carga
- 🔌 **Sistemas monofásico, bifásico e trifásico**
- 🧮 **Tabelas NBR 5410** — condutores de Cobre (Cu) e Alumínio (Al)
- 🌡️ **Fatores de correção** — temperatura ambiente e agrupamento de circuitos
- 📐 **Métodos de instalação** — B1, B2, C e D conforme NBR 5410
- 🔋 **Múltiplas cargas** com tipos individuais:
  - **Motor elétrico** → Fator de Potência + Rendimento + unidades CV/HP
  - **Carga resistiva** → Cálculo unitário (cos φ = 1,00)
  - **Carga geral / não identificada** → Fator de Potência global
- 📊 **Tabela comparativa** de bitolas (2 antes e 2 depois da recomendada)
- 📝 **Parecer técnico** em linguagem acessível com diagnóstico e seção recomendada
- 📄 **Exportação em PDF** com cabeçalho, parecer e memória de cálculo passo a passo
- 📱 **Design responsivo** para desktop e dispositivos móveis

---

## 🚀 Como Usar

### Online (recomendado)
Acesse diretamente: **[https://forestigam.github.io/Pr--Dimensionamento_El-trico/](https://forestigam.github.io/Pr--Dimensionamento_El-trico/)**

### Localmente
1. Baixe o arquivo `index.html`
2. Abra no navegador — **nenhuma instalação necessária**

---

## 🏗️ Tecnologias

| Tecnologia | Uso |
|---|---|
| HTML5 | Estrutura da página |
| CSS3 | Layout responsivo, glassmorphism, variáveis de cor |
| JavaScript (ES6) | Lógica de cálculo, renderização dinâmica dos cards |
| `document.createElement` | Cards de carga sem dependências externas |
| `window.print()` | Geração de PDF nativo |

> Aplicação **100% client-side** — não requer servidor, banco de dados ou login.

---

## 📐 Base Técnica

| Parâmetro | Referência |
|---|---|
| Capacidade de condução | Tabelas 36/37 da NBR 5410:2004 |
| Fator de temperatura | Tabela 40 |
| Fator de agrupamento | Tabela 41 |
| Limite de queda de tensão | §6.2.7 — máximo 4% em circuitos terminais |
| Resistividade do cobre | 0,021 Ω·mm²/m |
| Resistividade do alumínio | 0,035 Ω·mm²/m |

---

## ⚠️ Aviso Legal

Esta ferramenta realiza um **pré-dimensionamento** com base nos parâmetros informados. O resultado **não substitui** um projeto elétrico completo elaborado por **Engenheiro Elétrico habilitado pelo CREA/CFM**, nem a consulta à norma vigente ABNT NBR 5410 em sua versão mais atualizada.

---

## 📄 Licença

MIT License — uso livre para fins educacionais e profissionais.

---

<p align="center">
  Desenvolvido com ⚡ para profissionais de engenharia elétrica brasileiros
</p>

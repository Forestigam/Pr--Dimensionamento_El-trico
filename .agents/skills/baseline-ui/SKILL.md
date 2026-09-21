---
name: baseline-ui
description: Refinamento de layout, espaçamento (box model), hierarquia visual e tipografia para garantir coesão em telas de celular e PC.
---

# Baseline UI Skill

## Objetivos e Diretrizes
1. **Controle Estrito de Dimensões**:
   - Para folhas A4 (210mm x 297mm): o container base deve possuir `width: 794px` (ou `190mm` em áreas com margem).
   - Utilizar `box-sizing: border-box` estrito em todos os nós exportáveis para que paddings e bordas não causem overflow lateral.
2. **Prevenção de Cortes e Quebras de Texto**:
   - Manter `word-break: break-word` e `overflow-wrap: break-word`.
   - Garantir que elementos flex e grid internos não extrapolem o container pai.
3. **Escala Tipográfica Proporcional**:
   - Títulos técnicos: 1.2rem a 1.4rem.
   - Textos explicativos e parecer: 0.85rem a 0.95rem com line-height 1.6.
   - Blocos de código / memória: fontes monoespaçadas (Consolas, monospace) com tamanho legível (0.75rem a 0.8rem).

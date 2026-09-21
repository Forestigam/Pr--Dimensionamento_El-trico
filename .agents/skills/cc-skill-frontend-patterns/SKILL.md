---
name: cc-skill-frontend-patterns
description: Padrões de desenvolvimento front-end para React, Next.js e Vanilla JS. Gerenciamento de estado, responsividade e melhores práticas de UI mobile e desktop.
---

# Frontend Patterns Skill

## Objetivos e Diretrizes
1. **Responsividade Mobile-First**: Todos os componentes devem ser fluidos, utilizando unidades relativas (`rem`, `%`, `vw`, `vh`) ou wrappers flexíveis com `max-width` adequado.
2. **Gerenciamento de Estado**: Manter a sincronização entre entradas de dados (inputs, selects, sliders) e saídas calculadas em tempo real.
3. **Cross-Browser & Multi-Device**: Garantir suporte unificado para Safari (iOS), Chrome (Android/Desktop), Firefox e Edge, sem dependência de comportamentos proprietários que quebrem em telas menores.
4. **Isolamento de Estilos**: Evitar vazamento de regras CSS globais em componentes filhos ou iframes de impressão/exportação.

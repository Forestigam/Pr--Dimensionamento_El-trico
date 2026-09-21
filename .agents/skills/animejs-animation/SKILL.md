---
name: animejs-animation
description: Criação de animações web complexas e de alto desempenho, transições de estado e microinterações para relatórios e dashboards.
---

# AnimeJS Animation Skill

## Objetivos e Diretrizes
1. **Feedback Visual Imediato**: Transições suaves e animações de loading / status durante operações assíncronas (como cálculo elétrico em lote e geração de PDF).
2. **Performance Sem Reflows Pesados**: Priorizar transformações CSS (`transform`, `opacity`) para evitar reflows no DOM principal.
3. **Não-Bloqueio de Exportação**: Durante a captura de canvas ou exportação para PDF, desativar animações ou aguardar a estabilização completa do DOM.

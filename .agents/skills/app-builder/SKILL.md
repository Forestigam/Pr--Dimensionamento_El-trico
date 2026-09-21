---
name: app-builder
description: Orquestrador principal full-stack para estruturação de UI, integração de bibliotecas externas de exportação e coordenação geral da aplicação.
---

# App Builder Skill

## Objetivos e Diretrizes
1. **Integração de Bibliotecas Externas**:
   - Coordenação de bibliotecas de cliente como `html2pdf.js`, `html2canvas` e `jsPDF`.
   - Garantia de que scripts de terceiros sejam carregados de forma assíncrona com fallbacks seguros.
2. **Ciclo de Vida de Geração**:
   - Tratamento de exceções (try/catch abrangente com recuperação de estado da UI).
   - Abertura síncrona de nova aba no evento de clique para prevenir bloqueio de pop-ups em Safari/iOS.
   - Fornecimento de fallback de download direto caso o visualizador embutido encontre restrições de sandbox.

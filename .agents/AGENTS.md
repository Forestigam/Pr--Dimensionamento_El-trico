# Multi-Agent Architecture & Standards

Este projeto adota um comitê de inspeção e validação multi-agente composto por 6 papéis especializados:

## Agentes Especializados e Suas Atribuições

1. **`frontend_patterns_expert` (cc-skill-frontend-patterns)**:
   - Validação de padrões de layout, responsividade mobile/desktop e gerenciamento de estado.
2. **`antigravity_design_expert`**:
   - Engenharia de UI/UX, consistência de cores, hierarquia visual e estética técnica.
3. **`baseline_ui_expert`**:
   - Refinamento milimétrico de box-model (larguras, paddings, margins), tipografia e integridade de quebras de linha em celular e PC.
4. **`animejs_animation_expert`**:
   - Transições fluidas, microinterações e feedback assíncrono sem degradação do DOM.
5. **`app_builder_expert`**:
   - Orquestração full-stack, integração de bibliotecas externas (html2pdf, jsPDF, html2canvas) e arquitetura de componentes.
6. **`api_endpoint_builder_expert`**:
   - Pipelines de dados de engenharia NBR 5410, sanitização de strings e fidelidade da exportação de documentos.

## Protocolo de Comissionamento e Revisão
Toda alteração estrutural no código da aplicação ou no motor de geração de relatórios deve passar pelos critérios de cada um destes agentes antes de ser considerada concluída.

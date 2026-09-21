---
name: api-endpoint-builder
description: Estruturação e lógica de endpoints e pipelines de dados para processamento e geração de relatórios técnicos de engenharia em PDF.
---

# API Endpoint Builder Skill

## Objetivos e Diretrizes
1. **Pipeline de Dados do Relatório**:
   - Sanitização de strings HTML e caracteres especiais (`<`, `>`, `&`) na memória de cálculo e pareceres técnicos.
   - Preservação da formatação numérica segundo as normas ABNT (vírgula decimal pt-BR, unidades NBR 5410).
2. **Arquitetura de Geração de Documentos**:
   - Configuração determinística de renderização:
     - Formato A4 retrato (210mm x 297mm).
     - Mapeamento direto de coordenadas sem distorções de margens cumulativas.
     - Resolução nítida (scale: 2) para impressão limpa.

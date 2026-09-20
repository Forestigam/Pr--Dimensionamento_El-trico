"""
Gerador do App de Pré-Dimensionamento Elétrico NBR 5410
Estratégia limpa: HTML completo com placeholder __BG__ substituído pelo Python.
"""
import os

PASTA   = r"C:\Users\Edimar\.gemini\antigravity\scratch\Queda de tensão em Cabo - NBR 5410"
BG_PATH = r"C:\Users\Edimar\.gemini\antigravity\brain\e4f1c78c-fcf8-4a8a-a0af-b080a8242099\scratch\bg_base64.txt"

with open(BG_PATH, "r", encoding="utf-8") as f:
    BG_B64 = f.read().strip()

HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pré-Dimensionamento Elétrico — NBR 5410</title>
<style>
:root{
  --bg-dark:#0f172a;--panel-bg:rgba(30,41,59,0.85);--panel-border:rgba(255,255,255,0.1);
  --accent-blue:#3b82f6;--accent-cyan:#06b6d4;--accent-indigo:#6366f1;
  --status-green:#10b981;--status-yellow:#f59e0b;--status-red:#ef4444;
  --text-main:#f8fafc;--text-muted:#94a3b8;--card-bg:rgba(15,23,42,0.75);
}
*{box-sizing:border-box;margin:0;padding:0;font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,Roboto,sans-serif}
body{background-color:var(--bg-dark);color:var(--text-main);min-height:100vh;padding:20px 10px;position:relative}
body::before{content:"";position:fixed;inset:0;background-image:url('data:image/jpeg;base64,__BG__');background-size:cover;background-position:center;background-attachment:fixed;opacity:0.10;z-index:-1;pointer-events:none}
.container{max-width:1200px;margin:0 auto;display:flex;flex-direction:column;gap:24px}
header{background:linear-gradient(135deg,rgba(30,41,59,.9),rgba(15,23,42,.95));border:1px solid var(--panel-border);border-radius:16px;padding:24px;box-shadow:0 10px 30px rgba(0,0,0,.5);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px}
.brand-title{display:flex;align-items:center;gap:16px}
.brand-icon{width:48px;height:48px;background:linear-gradient(135deg,var(--accent-blue),var(--accent-cyan));border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:24px;box-shadow:0 4px 14px rgba(59,130,246,.4)}
.brand-text h1{font-size:1.5rem;font-weight:700;color:#fff;letter-spacing:-.5px}
.brand-text p{font-size:.85rem;color:var(--text-muted)}
.badge-norma{background:rgba(59,130,246,.15);border:1px solid rgba(59,130,246,.3);color:var(--accent-cyan);padding:6px 14px;border-radius:20px;font-size:.8rem;font-weight:600;letter-spacing:.5px}
.grid-2{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:24px}
@media(max-width:900px){.grid-2{grid-template-columns:1fr}}
.panel{background:var(--panel-bg);border:1px solid var(--panel-border);border-radius:16px;padding:24px;backdrop-filter:blur(12px);box-shadow:0 8px 32px rgba(0,0,0,.3)}
.panel-title{font-size:1.1rem;font-weight:600;color:#fff;margin-bottom:20px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(255,255,255,.08);padding-bottom:12px}
.panel-title-text{display:flex;align-items:center;gap:10px}
.panel-title span.step-num{background:var(--accent-blue);color:#fff;width:26px;height:26px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:.85rem;font-weight:700}
.form-group{display:flex;flex-direction:column;gap:6px;margin-bottom:16px}
.form-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px}
label{font-size:.85rem;font-weight:500;color:var(--text-muted);display:flex;align-items:center;justify-content:space-between}
input,select{width:100%;background:rgba(15,23,42,.8);border:1px solid rgba(255,255,255,.15);border-radius:8px;color:var(--text-main);padding:10px 12px;font-size:.9rem;transition:border-color .2s}
input:focus,select:focus{outline:none;border-color:var(--accent-blue)}
select option{background:#1e293b}
.range-container{display:flex;align-items:center;gap:10px}
.range-container input[type=range]{flex:1;accent-color:var(--accent-blue);height:4px}
.range-container input[type=number]{width:80px}
.btn{border:none;border-radius:10px;padding:10px 20px;font-size:.9rem;font-weight:600;cursor:pointer;transition:all .2s}
.btn-primary{background:linear-gradient(135deg,var(--accent-blue),var(--accent-indigo));color:#fff;box-shadow:0 4px 14px rgba(59,130,246,.4)}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 6px 20px rgba(59,130,246,.5)}
.btn-secondary{background:rgba(255,255,255,.08);color:var(--text-muted);border:1px solid rgba(255,255,255,.1)}
.btn-secondary:hover{background:rgba(255,255,255,.15);color:#fff}
.btn-add-load{width:100%;padding:12px;background:rgba(6,182,212,.1);border:1px dashed rgba(6,182,212,.4);border-radius:10px;color:var(--accent-cyan);font-size:.9rem;font-weight:600;cursor:pointer;margin-top:8px;transition:all .2s}
.btn-add-load:hover{background:rgba(6,182,212,.2)}
.btn-add-header{padding:6px 14px;background:rgba(6,182,212,.15);border:1px solid rgba(6,182,212,.3);border-radius:8px;color:var(--accent-cyan);font-size:.8rem;font-weight:600;cursor:pointer;white-space:nowrap}
.load-cards-container{display:flex;flex-direction:column;gap:16px;margin-bottom:16px}
.load-card{background:var(--card-bg);border:1px solid rgba(255,255,255,.12);border-radius:12px;padding:18px;position:relative;box-shadow:0 4px 16px rgba(0,0,0,.25)}
.load-card-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px dashed rgba(255,255,255,.1);padding-bottom:8px}
.load-card-title{font-weight:600;font-size:.95rem;color:var(--accent-cyan)}
.btn-remove-load{background:rgba(239,68,68,.15);border:1px solid rgba(239,68,68,.3);color:#ef4444;border-radius:6px;padding:4px 10px;font-size:.8rem;cursor:pointer}
.btn-remove-load:hover{background:rgba(239,68,68,.3)}
table{width:100%;border-collapse:collapse;font-size:.85rem}
th{background:rgba(59,130,246,.2);color:var(--accent-cyan);padding:10px 8px;text-align:left;font-weight:600;border-bottom:1px solid rgba(255,255,255,.1)}
td{padding:9px 8px;border-bottom:1px solid rgba(255,255,255,.05);color:var(--text-main)}
tr:hover td{background:rgba(255,255,255,.03)}
.highlight-suggest td{background:rgba(16,185,129,.12)!important;border-left:3px solid var(--status-green)}
.table-responsive{overflow-x:auto}
.metrics-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:16px}
.metric-card{background:var(--card-bg);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:14px;text-align:center}
.metric-label{font-size:.75rem;color:var(--text-muted);margin-bottom:6px}
.metric-value{font-size:1.3rem;font-weight:700;color:var(--accent-cyan)}
.result-badge{border-radius:12px;padding:16px 20px;margin-bottom:16px;border:1px solid;display:flex;align-items:center;gap:14px}
.result-badge.atende{background:rgba(16,185,129,.15);border-color:rgba(16,185,129,.4)}
.result-badge.nao-atende{background:rgba(239,68,68,.15);border-color:rgba(239,68,68,.4)}
.result-badge-icon{font-size:2.2rem;flex-shrink:0}
.result-badge-title{font-size:1.1rem;font-weight:700}
.result-badge.atende .result-badge-title{color:var(--status-green)}
.result-badge.nao-atende .result-badge-title{color:var(--status-red)}
.result-badge-sub{font-size:.85rem;opacity:.9;margin-top:4px}
.parecer-card{border-radius:10px;padding:16px 18px;margin-bottom:16px;border:1px solid;font-size:.9rem;line-height:1.7}
.parecer-card.atende{background:rgba(16,185,129,.1);border-color:rgba(16,185,129,.3)}
.parecer-card.nao-atende{background:rgba(239,68,68,.1);border-color:rgba(239,68,68,.3)}
.parecer-aprovado-destaque{background:rgba(16,185,129,.2);border:2px solid var(--status-green);border-radius:10px;padding:14px 18px;margin-top:12px;text-align:center;font-size:1.1rem;font-weight:700;color:var(--status-green);letter-spacing:.5px}
.accordion{border-radius:10px;overflow:hidden}
.accordion-header{background:rgba(59,130,246,.15);border:1px solid rgba(59,130,246,.2);padding:12px 16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-weight:600;color:#fff}
.accordion-header:hover{background:rgba(59,130,246,.25)}
.accordion-content{display:none;background:var(--card-bg);border:1px solid rgba(59,130,246,.2);border-top:none;padding:16px;font-family:'Consolas','Courier New',monospace;font-size:.78rem;white-space:pre-wrap;color:#cbd5e1;max-height:400px;overflow-y:auto}
.accordion-content.show{display:block}
.placeholder-panel{background:var(--panel-bg);border:1px solid var(--panel-border);border-radius:16px;padding:60px 24px;display:flex;flex-direction:column;align-items:center;gap:16px;text-align:center}
.placeholder-icon{font-size:3rem;opacity:.4}
.placeholder-title{font-size:1.3rem;font-weight:700;color:var(--text-muted)}
.placeholder-text{color:var(--text-muted);font-size:.9rem;max-width:400px;line-height:1.6}
.help-icon{cursor:help;font-size:.85rem;color:var(--accent-blue);margin-left:4px}
.al-warning{background:rgba(245,158,11,.15);border:1px solid rgba(245,158,11,.4);border-radius:8px;padding:10px 14px;font-size:.82rem;color:var(--status-yellow);margin-bottom:12px;display:none}
footer{background:rgba(15,23,42,.6);border:1px solid rgba(255,255,255,.06);border-radius:12px;padding:16px 20px;font-size:.8rem;color:var(--text-muted);text-align:center;line-height:1.6}
.btn-pdf{background:linear-gradient(135deg,#0f766e,#0891b2);color:#fff;border:none;border-radius:10px;padding:10px 20px;font-size:.88rem;font-weight:600;cursor:pointer;margin-top:12px}
.btn-pdf:hover{opacity:.9}
.tipo-tag{display:inline-block;font-size:.75rem;font-weight:600;padding:3px 8px;border-radius:6px;margin-left:8px;vertical-align:middle}
.tipo-motor{background:rgba(59,130,246,.25);color:#93c5fd}
.tipo-resistiva{background:rgba(245,158,11,.2);color:#fcd34d}
.tipo-geral{background:rgba(148,163,184,.2);color:#cbd5e1}
</style>
</head>
<body>
<div class="container">

<!-- HEADER -->
<header>
  <div class="brand-title">
    <div class="brand-icon">&#9889;</div>
    <div class="brand-text">
      <h1>Pré-Dimensionamento Elétrico</h1>
      <p>Circuitos de Baixa Tensão — Ferramenta Técnica para Engenheiros e Eletricistas</p>
    </div>
  </div>
  <div class="badge-norma">ABNT NBR 5410:2004</div>
</header>

<div class="grid-2">

<!-- ==================== COLUNA ESQUERDA ==================== -->
<div style="display:flex;flex-direction:column;gap:24px">

  <!-- Painel 1: Dados da Instalação -->
  <div class="panel">
    <div class="panel-title">
      <div class="panel-title-text"><span class="step-num">1</span> Dados da Instalação</div>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label>Material do Condutor</label>
        <select id="materialCondutor" onchange="onMaterialChange()">
          <option value="cu" selected>Cobre (Cu)</option>
          <option value="al">Alumínio (Al)</option>
        </select>
      </div>
      <div class="form-group">
        <label>Tipo de Isolação</label>
        <select id="isolacao" onchange="resetCalculado()">
          <option value="pvc" selected>PVC (70°C)</option>
          <option value="xlpe_epr">XLPE / EPR (90°C)</option>
        </select>
      </div>
    </div>

    <div id="alWarning" class="al-warning">&#9888; <strong>NBR 5410 §6.2.7.1:</strong> Condutores de alumínio não são permitidos para seções inferiores a 16 mm². As bitolas menores serão filtradas automaticamente nos resultados.</div>

    <div class="form-row">
      <div class="form-group">
        <label>Tensão (V) <span class="help-icon" title="Tensão de fase para sistemas monofásico/bifásico ou tensão de linha para trifásico">&#9432;</span></label>
        <div style="display:flex;gap:8px">
          <input type="number" id="tensao" value="220" min="100" step="1" style="flex:1" onchange="resetCalculado()">
          <select style="width:110px" onchange="document.getElementById('tensao').value=this.value;resetCalculado()">
            <option value="127">127 V</option>
            <option value="220" selected>220 V</option>
            <option value="380">380 V</option>
            <option value="440">440 V</option>
          </select>
        </div>
      </div>
      <div class="form-group">
        <label>Número de Fases</label>
        <select id="numeroFases" onchange="setFases(this.value)">
          <option value="mono" selected>Monofásico (1F + N)</option>
          <option value="bi">Bifásico (2F + N)</option>
          <option value="tri">Trifásico (3F + N)</option>
        </select>
      </div>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label>Distância do Circuito (m) <span class="help-icon" title="Comprimento do circuito em metros — somente números inteiros">&#9432;</span></label>
        <input type="number" id="distancia" value="30" min="1" step="1" oninput="validarDistanciaInteira(this)" onchange="resetCalculado()">
      </div>
      <div class="form-group">
        <label>Método de Instalação <span class="help-icon" title="B1 = Eletroduto embutido | B2 = Eletroduto sobreposto | C = Cabo fixado em parede/bandeja | D = Eletroduto enterrado">&#9432;</span></label>
        <select id="metodoInstalacao" onchange="resetCalculado()">
          <option value="b1" selected>B1 — Eletroduto embutido em parede</option>
          <option value="b2">B2 — Eletroduto sobreposto em parede</option>
          <option value="c">C — Cabo fixado em parede / bandeja</option>
          <option value="d">D — Eletroduto enterrado</option>
        </select>
      </div>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label>Temperatura Ambiente (°C)</label>
        <select id="temperatura" onchange="resetCalculado()">
          <option value="30" selected>30°C (referência da norma)</option>
          <option value="35">35°C</option>
          <option value="40">40°C</option>
          <option value="45">45°C</option>
          <option value="50">50°C</option>
        </select>
      </div>
      <div class="form-group">
        <label>Agrupamento de Circuitos</label>
        <select id="agrupamento" onchange="resetCalculado()">
          <option value="1" selected>1 circuito — Fator 1,00</option>
          <option value="2">2 circuitos — Fator 0,80</option>
          <option value="3">3 circuitos — Fator 0,70</option>
          <option value="4">4 circuitos — Fator 0,65</option>
          <option value="5">5 circuitos — Fator 0,60</option>
          <option value="6">6 circuitos — Fator 0,57</option>
          <option value="7">7 circuitos — Fator 0,54</option>
          <option value="8">8 ou mais circuitos — Fator 0,50</option>
        </select>
      </div>
    </div>

    <div class="form-group">
      <label for="fpGlobalNum">Fator de Potência Global (cos&nbsp;&#966;) &nbsp;<span id="fpGlobalLabel" style="color:var(--accent-cyan);font-weight:700">0,85</span></label>
      <div class="range-container">
        <input type="range" id="fpGlobalRange" min="0.15" max="1.00" step="0.01" value="0.85" oninput="syncGlobalFP('range',this.value)">
        <input type="number" id="fpGlobalNum" min="0.15" max="1.00" step="0.01" value="0.85" oninput="syncGlobalFP('num',this.value)">
      </div>
    </div>
  </div>

  <!-- Painel 2: Cargas do Circuito -->
  <div class="panel">
    <div class="panel-title">
      <div class="panel-title-text"><span class="step-num">2</span> Cargas do Circuito</div>
      <button type="button" class="btn-add-header" onclick="adicionarCarga()">+ Nova Carga</button>
    </div>

    <div id="loadCardsContainer" class="load-cards-container"></div>

    <button type="button" class="btn-add-load" onclick="adicionarCarga()">+ ADICIONAR CARGA AO CIRCUITO</button>

    <div class="table-responsive" style="margin-top:16px">
      <table>
        <thead>
          <tr>
            <th>Carga</th><th>Tipo</th><th>Especificação</th>
            <th style="text-align:right">Corrente</th>
            <th style="text-align:right">FP</th>
            <th style="text-align:right">Rend.</th>
            <th style="text-align:center">Qtd</th>
          </tr>
        </thead>
        <tbody id="tabelaResumoCargas"></tbody>
      </table>
    </div>
  </div>

  <!-- Painel 3: Condutor e Calcular -->
  <div class="panel">
    <div class="panel-title">
      <div class="panel-title-text"><span class="step-num">3</span> Condutor Comercial Testado</div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label for="secaoSelecionada">Seção Nominal do Condutor (mm²)</label>
        <select id="secaoSelecionada" onchange="resetCalculado()">
          <option value="1.5">1,5 mm²</option>
          <option value="2.5" selected>2,5 mm²</option>
          <option value="4">4,0 mm²</option>
          <option value="6">6,0 mm²</option>
          <option value="10">10,0 mm²</option>
          <option value="16">16,0 mm²</option>
          <option value="25">25,0 mm²</option>
          <option value="35">35,0 mm²</option>
          <option value="50">50,0 mm²</option>
          <option value="70">70,0 mm²</option>
          <option value="95">95,0 mm²</option>
          <option value="120">120,0 mm²</option>
          <option value="150">150,0 mm²</option>
          <option value="185">185,0 mm²</option>
          <option value="240">240,0 mm²</option>
        </select>
      </div>
      <div class="form-group">
        <label>Diâmetro Físico Aproximado <span class="help-icon" title="Informação dimensional complementar. O dimensionamento elétrico utiliza a seção em mm².">&#9432;</span></label>
        <input type="text" id="diametroAprox" value="1,78 mm" readonly style="background:rgba(255,255,255,.05);color:#cbd5e1">
      </div>
    </div>
    <div style="display:flex;gap:12px;margin-top:12px;flex-wrap:wrap">
      <button type="button" class="btn btn-primary" style="flex:1;font-size:1rem;padding:14px" onclick="executarCalculoClique()">&#9889; CALCULAR DIMENSIONAMENTO</button>
      <button type="button" class="btn btn-secondary" onclick="limpar()">&#128260; LIMPAR</button>
    </div>
  </div>

</div><!-- /coluna esquerda -->

<!-- ==================== COLUNA DIREITA ==================== -->
<div style="display:flex;flex-direction:column;gap:24px">

  <!-- Placeholder -->
  <div id="panelPlaceholder" class="placeholder-panel">
    <div class="placeholder-icon">&#9889;</div>
    <div class="placeholder-title">Aguardando Cálculo</div>
    <p class="placeholder-text">Preencha os dados da instalação e das cargas e clique em <strong>&#9889; CALCULAR DIMENSIONAMENTO</strong> para visualizar os resultados.</p>
  </div>

  <!-- Resultados -->
  <div id="containerResultados" style="display:none;flex-direction:column;gap:24px">

    <div class="panel">
      <div class="panel-title"><div class="panel-title-text"><span class="step-num">4</span> Resultado do Circuito</div></div>

      <div id="resultBadge" class="result-badge atende">
        <div class="result-badge-icon" id="resultIcon">&#9989;</div>
        <div>
          <div class="result-badge-title" id="resultTitle">ATENDE À NBR 5410</div>
          <div class="result-badge-sub" id="resultSub"></div>
        </div>
      </div>

      <div class="metrics-grid">
        <div class="metric-card"><div class="metric-label">Corrente de Projeto (Ib)</div><div class="metric-value" id="resIb">—</div></div>
        <div class="metric-card"><div class="metric-label">Capacidade Corrigida (Iz)</div><div class="metric-value" id="resIz">—</div></div>
        <div class="metric-card"><div class="metric-label">Tensão de Saída</div><div class="metric-value" id="resVsaida">—</div></div>
        <div class="metric-card"><div class="metric-label">Queda de Tensão (&#916;V)</div><div class="metric-value" id="resDeltaV">—</div></div>
        <div class="metric-card"><div class="metric-label">Queda Percentual (%)</div><div class="metric-value" id="resDeltaVPercent">—</div></div>
        <div class="metric-card"><div class="metric-label">Limite Máximo (NBR 5410)</div><div class="metric-value">4,00 %</div></div>
      </div>

      <div id="parecerCard" class="parecer-card atende">
        <div id="parecerTexto"></div>
      </div>
    </div>

    <div class="panel">
      <div class="panel-title">
        <span>&#128202; Comparativo de Bitolas Comerciais</span>
        <span style="font-size:.75rem;color:var(--text-muted);font-weight:normal">(2 bitolas antes e 2 depois da recomendada)</span>
      </div>
      <div class="table-responsive">
        <table>
          <thead><tr><th>Seção (mm²)</th><th>Iz Corrigida</th><th>Ib</th><th>&#916;V (V)</th><th>&#916;V (%)</th><th>Situação</th></tr></thead>
          <tbody id="tabelaBitolasComp"></tbody>
        </table>
      </div>
    </div>

    <div class="panel">
      <div class="accordion">
        <div class="accordion-header" onclick="toggleMemoria()">
          <span>&#128203; MEMÓRIA DE CÁLCULO — PASSO A PASSO</span>
          <span id="accordionArrow">&#9660;</span>
        </div>
        <div id="memoriaContent" class="accordion-content"></div>
      </div>
      <div style="text-align:right;margin-top:12px">
        <button class="btn-pdf" onclick="gerarPDF()">&#128196; GERAR PDF DA MEMÓRIA DE CÁLCULO</button>
      </div>
    </div>

  </div><!-- /containerResultados -->

</div><!-- /coluna direita -->
</div><!-- /grid-2 -->

<footer>
  <strong>Aviso técnico:</strong> Esta ferramenta realiza um pré-dimensionamento com base nos parâmetros informados e nos critérios implementados no aplicativo. O resultado <strong>não substitui</strong> um projeto elétrico completo, a consulta às tabelas e requisitos vigentes da ABNT NBR 5410, nem a avaliação por profissional habilitado.
</footer>

</div><!-- /container -->

<script>
/* =====================================================================
   TABELAS NBR 5410 — CAPACIDADE DE CONDUÇÃO (A)
   ===================================================================== */
var TABELA={
  cu:{
    pvc:{
      b1:{2:{1.5:17.5,2.5:24,4:32,6:41,10:57,16:76,25:101,35:125,50:151,70:192,95:232,120:269,150:300,185:341,240:400},3:{1.5:15.5,2.5:21,4:28,6:36,10:50,16:68,25:89,35:110,50:134,70:171,95:207,120:239,150:267,185:303,240:356}},
      b2:{2:{1.5:16.5,2.5:23,4:30,6:38,10:52,16:69,25:90,35:111,50:133,70:168,95:201,120:232,150:258,185:294,240:344},3:{1.5:15,2.5:20,4:27,6:34,10:46,16:62,25:80,35:99,50:118,70:149,95:179,120:206,150:225,185:258,240:301}},
      c:{2:{1.5:19.5,2.5:27,4:36,6:46,10:63,16:85,25:112,35:138,50:168,70:213,95:258,120:299,150:344,185:392,240:461},3:{1.5:17.5,2.5:24,4:32,6:41,10:57,16:76,25:96,35:119,50:144,70:184,95:223,120:259,150:299,185:341,240:403}},
      d:{2:{1.5:22,2.5:29,4:38,6:47,10:63,16:81,25:104,35:125,50:148,70:180,95:214,120:243,150:273,185:308,240:356},3:{1.5:18,2.5:24,4:31,6:39,10:52,16:67,25:86,35:103,50:122,70:149,95:177,120:201,150:226,185:255,240:295}}
    },
    xlpe_epr:{
      b1:{2:{1.5:22,2.5:31,4:42,6:54,10:75,16:100,25:133,35:164,50:198,70:253,95:306,120:354,150:393,185:449,240:528},3:{1.5:19,2.5:27,4:37,6:48,10:66,16:89,25:117,35:144,50:175,70:224,95:271,120:314,150:349,185:398,240:468}},
      b2:{2:{1.5:21,2.5:29,4:39,6:50,10:68,16:91,25:119,35:146,50:175,70:221,95:265,120:305,150:339,185:386,240:452},3:{1.5:18.5,2.5:26,4:35,6:44,10:60,16:80,25:105,35:129,50:154,70:194,95:233,120:268,150:297,185:338,240:394}},
      c:{2:{1.5:26,2.5:36,4:49,6:63,10:86,16:115,25:149,35:185,50:225,70:286,95:347,120:401,150:462,185:527,240:619},3:{1.5:23,2.5:32,4:43,6:55,10:75,16:100,25:127,35:158,50:192,70:246,95:298,120:346,150:399,185:456,240:538}},
      d:{2:{1.5:26,2.5:35,4:45,6:55,10:74,16:96,25:123,35:147,50:174,70:211,95:250,120:283,150:317,185:357,240:409},3:{1.5:22,2.5:29,4:37,6:46,10:61,16:79,25:101,35:121,50:143,70:174,95:206,120:234,150:262,185:294,240:338}}
    }
  },
  al:{
    pvc:{
      b1:{2:{16:59,25:78,35:96,50:117,70:148,95:180,120:208,150:232,185:264,240:310},3:{16:52,25:69,35:85,50:103,70:131,95:160,120:185,150:206,185:235,240:275}},
      b2:{2:{16:53,25:70,35:86,50:103,70:130,95:156,120:180,150:200,185:228,240:267},3:{16:47,25:62,35:76,50:91,70:115,95:138,120:159,150:174,185:199,240:233}},
      c:{2:{16:66,25:87,35:107,50:131,70:166,95:201,120:233,150:268,185:306,240:360},3:{16:59,25:75,35:93,50:113,70:144,95:175,120:203,150:234,185:267,240:316}},
      d:{2:{16:63,25:81,35:97,50:115,70:140,95:166,120:189,150:212,185:239,240:276},3:{16:52,25:67,35:80,50:95,70:115,95:137,120:156,150:175,185:197,240:228}}
    },
    xlpe_epr:{
      b1:{2:{16:78,25:103,35:127,50:154,70:197,95:238,120:275,150:306,185:349,240:411},3:{16:69,25:91,35:112,50:136,70:174,95:211,120:244,150:271,185:309,240:364}},
      b2:{2:{16:71,25:92,35:113,50:136,70:172,95:206,120:237,150:263,185:300,240:351},3:{16:62,25:81,35:100,50:120,70:151,95:181,120:208,150:231,185:263,240:307}},
      c:{2:{16:89,25:116,35:144,50:175,70:223,95:270,120:312,150:359,185:410,240:482},3:{16:78,25:99,35:123,50:150,70:192,95:232,120:269,150:310,185:355,240:419}},
      d:{2:{16:75,25:96,35:114,50:135,70:164,95:194,120:220,150:246,185:277,240:318},3:{16:62,25:79,35:94,50:111,70:135,95:160,120:182,150:203,185:228,240:262}}
    }
  }
};
var FTEMP={pvc:{30:1.00,35:0.94,40:0.87,45:0.79,50:0.71},xlpe_epr:{30:1.00,35:0.96,40:0.91,45:0.87,50:0.82}};
var FAGRUP={1:1.00,2:0.80,3:0.70,4:0.65,5:0.60,6:0.57,7:0.54,8:0.50};
var DIAM={1.5:"1,38 mm",2.5:"1,78 mm",4:"2,26 mm",6:"2,76 mm",10:"3,57 mm",16:"4,51 mm",25:"5,64 mm",35:"6,68 mm",50:"7,98 mm",70:"9,44 mm",95:"11,00 mm",120:"12,36 mm",150:"13,82 mm",185:"15,35 mm",240:"17,48 mm"};
var SECOES=[1.5,2.5,4,6,10,16,25,35,50,70,95,120,150,185,240];

var estadoFases='mono', cargas=[], contadorId=1, memoriaGlobal='', parecerGlobal='';

/* =====================================================================
   HELPERS
   ===================================================================== */
function validarDistanciaInteira(el){
  var v=el.value.replace(/[^0-9]/g,'');
  el.value=(!v||parseInt(v,10)<1)?'1':v;
}
function setFases(f){estadoFases=f;var el=document.getElementById('numeroFases');if(el)el.value=f;resetCalculado();}
function syncGlobalFP(src,val){
  var n=parseFloat(val);if(isNaN(n))n=0.85;
  n=Math.max(0.15,Math.min(1.00,n));
  var r=document.getElementById('fpGlobalRange'),i=document.getElementById('fpGlobalNum'),l=document.getElementById('fpGlobalLabel');
  if(src==='range'&&i)i.value=n.toFixed(2);
  if(src==='num'&&r)r.value=n;
  if(l)l.textContent=n.toFixed(2).replace('.',',');
  resetCalculado();
}
function onMaterialChange(){
  document.getElementById('alWarning').style.display=document.getElementById('materialCondutor').value==='al'?'block':'none';
  resetCalculado();
}
function resetCalculado(){
  document.getElementById('containerResultados').style.display='none';
  document.getElementById('panelPlaceholder').style.display='flex';
}
function executarCalculoClique(){
  document.getElementById('panelPlaceholder').style.display='none';
  document.getElementById('containerResultados').style.display='flex';
  calcular();
}

/* =====================================================================
   GERENCIAMENTO DE CARGAS
   ===================================================================== */
function adicionarCarga(nome,tipoCarga,modo,valorPot,unidadePot,fp,rend,qtd){
  var id='c'+(contadorId++);
  cargas.push({
    id:id,
    nome:nome||('Carga #'+(cargas.length+1)),
    tipoCarga:tipoCarga||'motor',
    modo:modo||'potencia',
    valorPot:typeof valorPot==='number'?valorPot:5,
    unidadePot:unidadePot||'CV',
    correnteNom:10,
    fp:typeof fp==='number'?fp:0.85,
    rend:typeof rend==='number'?rend:90,
    qtd:typeof qtd==='number'?qtd:1
  });
  renderCards();
  resetCalculado();
}

function removerCarga(id){
  if(cargas.length<=1){alert('O circuito deve ter pelo menos uma carga cadastrada.');return;}
  cargas=cargas.filter(function(c){return c.id!==id;});
  renderCards();resetCalculado();
}

function atualizarCarga(id,campo,valor){
  var c=cargas.find(function(x){return x.id===id;});
  if(!c)return;
  c[campo]=valor;
  if(campo==='tipoCarga'){
    // Ao mudar tipo, ajustar unidade e valores padrão
    if(valor!=='motor'&&(c.unidadePot==='CV'||c.unidadePot==='HP'))c.unidadePot='kW';
    renderCards();
  } else if(campo==='modo'){
    renderCards();
  }
  resetCalculado();
}

function syncFP(id,src,val){
  var n=parseFloat(val);if(isNaN(n))n=0.85;n=Math.max(0.15,Math.min(1.00,n));
  var c=cargas.find(function(x){return x.id===id;});if(c)c.fp=n;
  if(src==='range'){var el=document.getElementById('fpN_'+id);if(el)el.value=n.toFixed(2);}
  else            {var el=document.getElementById('fpR_'+id);if(el)el.value=n;}
  resetCalculado();
}

function syncRend(id,src,val){
  var n=parseFloat(val);if(isNaN(n))n=90;n=Math.max(10,Math.min(100,n));
  var c=cargas.find(function(x){return x.id===id;});if(c)c.rend=n;
  if(src==='range'){var el=document.getElementById('rN_'+id);if(el)el.value=Math.round(n);}
  else            {var el=document.getElementById('rR_'+id);if(el)el.value=n;}
  resetCalculado();
}

/* =====================================================================
   RENDERIZAÇÃO DOS CARDS — document.createElement (sem aspas aninhadas)
   ===================================================================== */
function renderCards(){
  var cont=document.getElementById('loadCardsContainer');
  if(!cont)return;
  cont.innerHTML='';

  cargas.forEach(function(carga,idx){
    var id        =carga.id;
    var fpVal     =isNaN(carga.fp)?0.85:carga.fp;
    var rendVal   =isNaN(carga.rend)?90:carga.rend;
    var potVal    =isNaN(carga.valorPot)?5:carga.valorPot;
    var iNomVal   =isNaN(carga.correnteNom)?10:carga.correnteNom;
    var qtdVal    =isNaN(carga.qtd)?1:carga.qtd;
    var tipoVal   =carga.tipoCarga||'motor';
    var modoVal   =carga.modo||'potencia';
    var unidVal   =carga.unidadePot||'CV';
    var nomeVal   =carga.nome||('Carga #'+(idx+1));
    var ehMotor   =(tipoVal==='motor');

    var card=document.createElement('div');card.className='load-card';

    /* ----- Header ----- */
    var hdr=document.createElement('div');hdr.className='load-card-header';
    var ttl=document.createElement('span');ttl.className='load-card-title';
    var tipoLabel=tipoVal==='motor'?'Motor':tipoVal==='resistiva'?'Resistiva':'Geral';
    var tipoClass=tipoVal==='motor'?'tipo-motor':tipoVal==='resistiva'?'tipo-resistiva':'tipo-geral';
    ttl.innerHTML='&#9889; Item #'+(idx+1)+'&nbsp;&mdash;&nbsp;'+nomeVal
      +'<span class="tipo-tag '+tipoClass+'">'+tipoLabel+'</span>';
    hdr.appendChild(ttl);
    if(cargas.length>1){
      var btnR=document.createElement('button');btnR.className='btn-remove-load';btnR.innerHTML='&#128465; Remover';
      (function(cid){btnR.addEventListener('click',function(){removerCarga(cid);});})(id);
      hdr.appendChild(btnR);
    }
    card.appendChild(hdr);

    /* ----- Nome da Carga ----- */
    var gNome=document.createElement('div');gNome.className='form-group';gNome.style.marginBottom='12px';
    var lNome=document.createElement('label');lNome.textContent='Identificação / Nome da Carga';
    var iNome=document.createElement('input');iNome.type='text';iNome.value=nomeVal;iNome.placeholder='Ex.: Motor Bomba, Compressor, Iluminação';
    (function(cid){iNome.addEventListener('change',function(){atualizarCarga(cid,'nome',this.value);});})(id);
    gNome.appendChild(lNome);gNome.appendChild(iNome);card.appendChild(gNome);

    /* ----- Tipo de Carga ----- */
    var rTipo=document.createElement('div');rTipo.className='form-row';
    var gTipo=document.createElement('div');gTipo.className='form-group';
    var lTipo=document.createElement('label');lTipo.textContent='Tipo de Carga';
    var sTipo=document.createElement('select');
    [['motor','Motor El\u00e9trico'],['resistiva','Carga Resistiva (Chuveiro, Aquecedor, L\u00e2mpada)'],['nao_id','Carga Geral / N\u00e3o Identificada']].forEach(function(o){
      var op=document.createElement('option');op.value=o[0];op.textContent=o[1];
      if(tipoVal===o[0])op.selected=true;sTipo.appendChild(op);
    });
    (function(cid){sTipo.addEventListener('change',function(){atualizarCarga(cid,'tipoCarga',this.value);});})(id);
    gTipo.appendChild(lTipo);gTipo.appendChild(sTipo);rTipo.appendChild(gTipo);

    /* ----- Modo de Especificação ----- */
    var gModo=document.createElement('div');gModo.className='form-group';
    var lModo=document.createElement('label');lModo.textContent='Modo de Especifica\u00e7\u00e3o';
    var sModo=document.createElement('select');
    [['potencia','Usar Pot\u00eancia'],['corrente','Usar Corrente Nominal (A)']].forEach(function(o){
      var op=document.createElement('option');op.value=o[0];op.textContent=o[1];
      if(modoVal===o[0])op.selected=true;sModo.appendChild(op);
    });
    (function(cid){sModo.addEventListener('change',function(){atualizarCarga(cid,'modo',this.value);});})(id);
    gModo.appendChild(lModo);gModo.appendChild(sModo);rTipo.appendChild(gModo);
    card.appendChild(rTipo);

    /* ----- Potência ou Corrente + Qtd ----- */
    var rPot=document.createElement('div');rPot.className='form-row';

    if(modoVal==='potencia'){
      var gPot=document.createElement('div');gPot.className='form-group';
      var lPot=document.createElement('label');lPot.textContent='Pot\u00eancia Nominal';
      var wPot=document.createElement('div');wPot.style.cssText='display:flex;gap:8px';
      var iPot=document.createElement('input');iPot.type='number';iPot.value=potVal;iPot.min='0.01';iPot.step='0.01';iPot.style.flex='1';
      (function(cid){iPot.addEventListener('change',function(){atualizarCarga(cid,'valorPot',parseFloat(this.value)||0);});})(id);
      var sUni=document.createElement('select');sUni.style.width='80px';
      // Motor: W, kW, CV, HP — Resistiva/Geral: W, kW
      var unidades=ehMotor?[['W','W'],['kW','kW'],['CV','CV'],['HP','HP']]:[['W','W'],['kW','kW']];
      unidades.forEach(function(u){
        var op=document.createElement('option');op.value=u[0];op.textContent=u[1];
        if(unidVal===u[0])op.selected=true;sUni.appendChild(op);
      });
      (function(cid){sUni.addEventListener('change',function(){atualizarCarga(cid,'unidadePot',this.value);});})(id);
      wPot.appendChild(iPot);wPot.appendChild(sUni);
      gPot.appendChild(lPot);gPot.appendChild(wPot);rPot.appendChild(gPot);
    } else {
      var gCor=document.createElement('div');gCor.className='form-group';
      var lCor=document.createElement('label');lCor.textContent='Corrente Nominal (A)';
      var iCor=document.createElement('input');iCor.type='number';iCor.value=iNomVal;iCor.min='0.1';iCor.step='0.1';
      (function(cid){iCor.addEventListener('change',function(){atualizarCarga(cid,'correnteNom',parseFloat(this.value)||0);});})(id);
      gCor.appendChild(lCor);gCor.appendChild(iCor);rPot.appendChild(gCor);
    }

    var gQtd=document.createElement('div');gQtd.className='form-group';
    var lQtd=document.createElement('label');lQtd.textContent='Quantidade';
    var iQtd=document.createElement('input');iQtd.type='number';iQtd.value=qtdVal;iQtd.min='1';iQtd.step='1';
    (function(cid){iQtd.addEventListener('change',function(){atualizarCarga(cid,'qtd',parseInt(this.value)||1);});})(id);
    gQtd.appendChild(lQtd);gQtd.appendChild(iQtd);rPot.appendChild(gQtd);
    card.appendChild(rPot);

    /* ----- FP (apenas Motor) ----- */
    if(ehMotor){
      var gFP=document.createElement('div');gFP.className='form-group';
      var lFP=document.createElement('label');lFP.textContent='Fator de Pot\u00eancia da Carga (cos \u03c6)';
      var cFP=document.createElement('div');cFP.className='range-container';
      var fpR=document.createElement('input');fpR.type='range';fpR.id='fpR_'+id;fpR.min='0.15';fpR.max='1.00';fpR.step='0.01';fpR.value=fpVal;
      var fpN=document.createElement('input');fpN.type='number';fpN.id='fpN_'+id;fpN.min='0.15';fpN.max='1.00';fpN.step='0.01';fpN.value=fpVal.toFixed(2);fpN.style.width='75px';
      (function(cid){
        fpR.addEventListener('input',function(){syncFP(cid,'range',this.value);});
        fpN.addEventListener('input',function(){syncFP(cid,'num',this.value);});
      })(id);
      cFP.appendChild(fpR);cFP.appendChild(fpN);gFP.appendChild(lFP);gFP.appendChild(cFP);card.appendChild(gFP);

      /* ----- Rendimento (Motor + modo Potência) ----- */
      if(modoVal==='potencia'){
        var gRend=document.createElement('div');gRend.className='form-group';
        var lRend=document.createElement('label');lRend.textContent='Rendimento do Motor \u03b7 (%)';
        var cRend=document.createElement('div');cRend.className='range-container';
        var rR=document.createElement('input');rR.type='range';rR.id='rR_'+id;rR.min='10';rR.max='100';rR.step='1';rR.value=rendVal;
        var rN=document.createElement('input');rN.type='number';rN.id='rN_'+id;rN.min='10';rN.max='100';rN.step='1';rN.value=Math.round(rendVal);rN.style.width='75px';
        (function(cid){
          rR.addEventListener('input',function(){syncRend(cid,'range',this.value);});
          rN.addEventListener('input',function(){syncRend(cid,'num',this.value);});
        })(id);
        cRend.appendChild(rR);cRend.appendChild(rN);gRend.appendChild(lRend);gRend.appendChild(cRend);card.appendChild(gRend);
      }
    }

    cont.appendChild(card);
  });
}

/* =====================================================================
   CÁLCULO PRINCIPAL
   ===================================================================== */
function calcular(){
  var material =document.getElementById('materialCondutor').value;
  var isolacao  =document.getElementById('isolacao').value;
  var V         =parseFloat(document.getElementById('tensao').value)||220;
  var dist      =parseInt(document.getElementById('distancia').value,10)||30;
  var fpGlobal  =parseFloat(document.getElementById('fpGlobalNum').value)||0.85;
  var metodo    =document.getElementById('metodoInstalacao').value;
  var condC     =estadoFases==='tri'?3:2;
  var temp      =document.getElementById('temperatura').value;
  var agrup     =document.getElementById('agrupamento').value;
  var secaoSel  =parseFloat(document.getElementById('secaoSelecionada').value)||2.5;

  document.getElementById('diametroAprox').value=DIAM[secaoSel]||'N/D';

  var fTemp =FTEMP[isolacao][parseInt(temp,10)]||1.0;
  var fAgrup=FAGRUP[parseInt(agrup,10)]||1.0;
  var fTotal=fTemp*fAgrup;
  var rho   =material==='cu'?0.021:0.035;

  /* --- Cargas --- */
  var P_total=0,Q_total=0;
  var tbody=document.getElementById('tabelaResumoCargas');
  tbody.innerHTML='';

  cargas.forEach(function(c,i){
    var tipoC=c.tipoCarga||'motor';
    var ehMotor=(tipoC==='motor');
    var fp_c=ehMotor?Math.max(0.15,Math.min(1.00,c.fp||0.85)):0.97;
    var rend_c=ehMotor&&c.modo==='potencia'?Math.max(0.10,Math.min(1.00,(c.rend||90)/100)):0.97;

    var I_c=0,P_c=0,especStr='';
    if(c.modo==='potencia'){
      var v=c.valorPot||0,u=c.unidadePot||'kW';
      var factor=u==='kW'?1000:u==='CV'?735.5:u==='HP'?745.7:1;
      var potW=v*factor;
      P_c=potW*(c.qtd||1);
      I_c=estadoFases==='tri'?P_c/(Math.sqrt(3)*V*fp_c*rend_c):P_c/(V*fp_c*rend_c);
      especStr=v.toLocaleString('pt-BR')+' '+u+' ('+(P_c/1000).toFixed(2)+' kW)';
    } else {
      I_c=(c.correnteNom||0)*(c.qtd||1);
      P_c=estadoFases==='tri'?Math.sqrt(3)*V*I_c*fp_c:V*I_c*fp_c;
      especStr='Corrente: '+I_c.toFixed(2)+' A';
    }
    var phi=Math.acos(fp_c);
    P_total+=P_c;Q_total+=P_c*Math.tan(phi);

    var tipoLabel=tipoC==='motor'?'Motor':tipoC==='resistiva'?'Resistiva':'Geral';
    var tr=document.createElement('tr');
    tr.innerHTML='<td>'+(c.nome||('Carga #'+(i+1)))+'</td>'
      +'<td>'+tipoLabel+'</td>'
      +'<td>'+especStr+'</td>'
      +'<td style="text-align:right">'+I_c.toFixed(2)+' A</td>'
      +'<td style="text-align:right">'+fp_c.toFixed(2)+'</td>'
      +'<td style="text-align:right">'+(ehMotor&&c.modo==='potencia'?Math.round(c.rend||90)+'%':'-')+'</td>'
      +'<td style="text-align:center">'+(c.qtd||1)+'</td>';
    tbody.appendChild(tr);
  });

  var S_total=Math.sqrt(P_total*P_total+Q_total*Q_total);
  var fp_eq  =S_total>0?P_total/S_total:1.0;
  var Ib     =estadoFases==='tri'?S_total/(Math.sqrt(3)*V):S_total/V;

  /* --- Avaliação de seção --- */
  function avaliarSecao(s){
    var tabMat=TABELA[material][isolacao][metodo];if(!tabMat)return null;
    var tabCC=tabMat[condC]||tabMat[2];var Iz_base=tabCC?tabCC[s]:null;if(!Iz_base)return null;
    var Iz_corr=Iz_base*fTotal;
    var coeff=estadoFases==='tri'?Math.sqrt(3):2;
    var dV=(coeff*dist*Ib*rho)/s;var dVp=(dV/V)*100;
    return{secao:s,Iz_base:Iz_base,Iz_corrigida:Iz_corr,deltaV:dV,deltaVPercent:dVp,atendeCorrente:Iz_corr>=Ib,atendeQueda:dVp<=4.0,atendeGeral:Iz_corr>=Ib&&dVp<=4.0};
  }

  var resAtual=avaliarSecao(secaoSel);
  var secaoSuger=null;
  SECOES.forEach(function(s){
    if(material==='al'&&s<16)return;
    var r=avaliarSecao(s);
    if(r&&r.atendeGeral&&!secaoSuger)secaoSuger=r;
  });

  if(!resAtual){document.getElementById('resIb').textContent='Erro — seção não encontrada nas tabelas.';return;}

  /* --- Métricas --- */
  document.getElementById('resIb').textContent           =Ib.toFixed(2)+' A';
  document.getElementById('resIz').textContent           =resAtual.Iz_corrigida.toFixed(2)+' A';
  document.getElementById('resVsaida').textContent       =(V-resAtual.deltaV).toFixed(2)+' V';
  document.getElementById('resDeltaV').textContent       =resAtual.deltaV.toFixed(2)+' V';
  document.getElementById('resDeltaVPercent').textContent=resAtual.deltaVPercent.toFixed(2)+' %';

  /* --- Badge de status --- */
  var badge      =document.getElementById('resultBadge');
  var iconEl     =document.getElementById('resultIcon');
  var titleEl    =document.getElementById('resultTitle');
  var subEl      =document.getElementById('resultSub');
  var parecerCard=document.getElementById('parecerCard');
  var parecerDiv =document.getElementById('parecerTexto');

  var secaoSelStr=secaoSel.toLocaleString('pt-BR')+' mm\u00b2';

  if(resAtual.atendeGeral){
    badge.className='result-badge atende';
    iconEl.textContent='\u2705';  // ✅
    titleEl.style.color='var(--status-green)';
    titleEl.textContent='ATENDE \u00c0 NBR 5410';
    subEl.textContent='O cabo de '+secaoSelStr+' satisfaz todos os crit\u00e9rios da norma para este circuito.';
    parecerCard.className='parecer-card atende';
    parecerDiv.innerHTML=
      '\u2705 <strong>PARECER T\u00c9CNICO:</strong> O cabo selecionado de <strong>'+secaoSelStr+'</strong> atende os requisitos de queda de tens\u00e3o e condu\u00e7\u00e3o de corrente el\u00e9trica exigidos pela NBR 5410. '
      +'A capacidade de condu\u00e7\u00e3o corrigida \u00e9 de <strong>'+resAtual.Iz_corrigida.toFixed(2)+' A</strong>, superior \u00e0 corrente de projeto de <strong>'+Ib.toFixed(2)+' A</strong>. '
      +'A queda de tens\u00e3o calculada \u00e9 de <strong>'+resAtual.deltaV.toFixed(2)+' V ('+resAtual.deltaVPercent.toFixed(2)+'%)</strong>, dentro do limite m\u00e1ximo de 4,00%. '
      +'Voc\u00ea pode executar o projeto com seguran\u00e7a!'
      +'<div class="parecer-aprovado-destaque">\ud83d\udfe2 PARAB\u00c9NS! SEU PROJETO EST\u00c1 APROVADO!</div>';
    parecerGlobal='PARECER T\u00c9CNICO:\nO cabo selecionado de '+secaoSelStr+' atende os requisitos de queda de tens\u00e3o e condu\u00e7\u00e3o de corrente el\u00e9trica exigidos pela NBR 5410.\nCapacidade corrigida Iz = '+resAtual.Iz_corrigida.toFixed(2)+' A >= Ib = '+Ib.toFixed(2)+' A.\nQueda de tens\u00e3o \u0394V = '+resAtual.deltaV.toFixed(2)+' V ('+resAtual.deltaVPercent.toFixed(2)+'%) <= 4,00%.\nPROJETO APROVADO!';
  } else {
    badge.className='result-badge nao-atende';
    iconEl.textContent='\u274c';  // ❌
    titleEl.style.color='var(--status-red)';
    titleEl.textContent='N\u00c3O ATENDE \u00c0 NBR 5410';
    subEl.textContent='O cabo de '+secaoSelStr+' n\u00e3o satisfaz todos os crit\u00e9rios. Verifique o parecer t\u00e9cnico abaixo.';

    var diagHtml='', diagTxt='';

    if(!resAtual.atendeCorrente){
      diagHtml+='<p style="margin-bottom:10px">\u26a1 <strong>Capacidade de condu\u00e7\u00e3o insuficiente:</strong> '
        +'O cabo condutor selecionado (<strong>'+secaoSelStr+'</strong>) n\u00e3o \u00e9 suficiente para conduzir a corrente do seu projeto. '
        +'Seu projeto exige <strong>'+Ib.toFixed(2)+' A</strong> e a capacidade m\u00e1xima do cabo selecionado \u00e9 de apenas <strong>'+resAtual.Iz_corrigida.toFixed(2)+' A</strong>.</p>';
      diagTxt+='- Capacidade de condu\u00e7\u00e3o insuficiente: cabo de '+secaoSelStr+' suporta '+resAtual.Iz_corrigida.toFixed(2)+' A, mas o projeto exige '+Ib.toFixed(2)+' A.\n';
    }
    if(!resAtual.atendeQueda){
      diagHtml+='<p style="margin-bottom:10px">\ud83d\udcc9 <strong>Queda de tens\u00e3o excessiva:</strong> '
        +'A queda de tens\u00e3o no seu projeto \u00e9 de <strong>'+resAtual.deltaV.toFixed(2)+' V ('+resAtual.deltaVPercent.toFixed(2)+'%)</strong>, '
        +'que est\u00e1 acima do valor m\u00e1ximo permitido pela NBR 5410, que \u00e9 de <strong>4,00% ('+((V*0.04).toFixed(2))+' V)</strong>.</p>';
      diagTxt+='- Queda de tens\u00e3o excessiva: '+resAtual.deltaVPercent.toFixed(2)+'% ('+resAtual.deltaV.toFixed(2)+' V) > limite de 4,00% ('+(V*0.04).toFixed(2)+' V).\n';
    }

    var recHtml='', recTxt='';
    if(secaoSuger){
      recHtml='<div style="margin-top:12px;padding:12px 14px;background:rgba(16,185,129,.15);border:1px solid rgba(16,185,129,.4);border-radius:8px">'
        +'\u2705 <strong>SE\u00c7\u00c3O RECOMENDADA:</strong> '
        +'Para que seu projeto atenda os requisitos b\u00e1sicos da norma, voc\u00ea deve trocar o cabo para <strong>'+secaoSuger.secao.toLocaleString('pt-BR')+' mm\u00b2</strong>. '
        +'Com esse cabo, a capacidade de condu\u00e7\u00e3o ser\u00e1 de <strong>'+secaoSuger.Iz_corrigida.toFixed(2)+' A</strong> '
        +'e a queda de tens\u00e3o ser\u00e1 de <strong>'+secaoSuger.deltaVPercent.toFixed(2)+'%</strong> \u2014 ambos dentro dos limites da NBR 5410.'
        +'<div class="parecer-aprovado-destaque" style="margin-top:10px">\ud83d\udfe2 Com este cabo, seu projeto estar\u00e1 APROVADO!</div>'
        +'</div>';
      recTxt='\nSE\u00c7\u00c3O RECOMENDADA: '+secaoSuger.secao.toLocaleString('pt-BR')+' mm\u00b2 (Iz = '+secaoSuger.Iz_corrigida.toFixed(2)+' A | \u0394V% = '+secaoSuger.deltaVPercent.toFixed(2)+'%).';
    } else {
      recHtml='<p style="margin-top:10px;color:var(--status-yellow)">\u26a0\ufe0f <strong>Aten\u00e7\u00e3o:</strong> Nenhuma bitola comercial at\u00e9 240 mm\u00b2 atende os crit\u00e9rios. Recomenda-se subdividir o circuito ou elevar o n\u00edvel de tens\u00e3o.</p>';
      recTxt='\nNENHUMA SE\u00c7\u00c3O DISPON\u00cdVEL atende at\u00e9 240 mm\u00b2. Subdivida o circuito ou eleve a tens\u00e3o.';
    }

    parecerCard.className='parecer-card nao-atende';
    parecerDiv.innerHTML='<strong>\ud83d\udd34 PARECER T\u00c9CNICO \u2014 DIAGN\u00d3STICO:</strong><br><br>'+diagHtml+recHtml;
    parecerGlobal='PARECER T\u00c9CNICO - DIAGN\u00d3STICO:\n'+diagTxt+recTxt;
  }

  /* --- Tabela comparativa (2 antes + 2 depois da recomendada) --- */
  var tbody2=document.getElementById('tabelaBitolasComp');
  tbody2.innerHTML='';
  var secRef=secaoSuger?secaoSuger.secao:secaoSel;
  var idxRef=SECOES.indexOf(secRef);if(idxRef<0)idxRef=SECOES.indexOf(secaoSel);
  var ini=Math.max(0,idxRef-2),fim=Math.min(SECOES.length-1,idxRef+2);
  for(var si=ini;si<=fim;si++){
    var s=SECOES[si];if(material==='al'&&s<16)continue;
    var ev=avaliarSecao(s);if(!ev)continue;
    var isSel=(s===secaoSel),isSug=(secaoSuger&&s===secaoSuger.secao);
    var tr2=document.createElement('tr');
    if(isSug||(isSel&&ev.atendeGeral))tr2.className='highlight-suggest';
    tr2.innerHTML='<td><strong>'+s.toLocaleString('pt-BR')+' mm\u00b2</strong>'+(isSel?' \ud83d\udccc <i>(Atual)</i>':'')+(isSug?' \u2b50 <i>(Recomendada)</i>':'')+'</td>'
      +'<td>'+ev.Iz_corrigida.toFixed(2)+' A</td>'
      +'<td>'+Ib.toFixed(2)+' A</td>'
      +'<td>'+ev.deltaV.toFixed(2)+' V</td>'
      +'<td>'+ev.deltaVPercent.toFixed(2)+' %</td>'
      +'<td>'+(ev.atendeGeral?'\ud83d\udfe2 \u2705 OK':'\ud83d\udd34 \u274c Reprovado')+'</td>';
    tbody2.appendChild(tr2);
  }

  /* --- Memória de Cálculo --- */
  var faseStr=estadoFases==='mono'?'Monof\u00e1sico':estadoFases==='bi'?'Bif\u00e1sico':'Trif\u00e1sico';
  var coefStr=estadoFases==='tri'?'1,73205':'2';
  memoriaGlobal=
'======================================================================\n'
+'      MEM\u00d3RIA DE C\u00c1LCULO \u2014 PR\u00c9-DIMENSIONAMENTO EL\u00c9TRICO\n'
+'                    ABNT NBR 5410:2004\n'
+'======================================================================\n\n'
+'1. C\u00c1LCULO DA CORRENTE DE PROJETO (Ib)\n'
+'----------------------------------------------------------------------\n'
+'  Pot\u00eancia Ativa Total  P = '+(P_total/1000).toFixed(3)+' kW\n'
+'  Pot\u00eancia Reativa Total Q = '+(Q_total/1000).toFixed(3)+' kVAR\n'
+'  Pot\u00eancia Aparente Total S = '+(S_total/1000).toFixed(3)+' kVA\n'
+'  Fator de Pot\u00eancia Equivalente FPeq = '+fp_eq.toFixed(4)+'\n'
+'  Sistema: '+faseStr+' \u2014 '+V+' V\n\n'
+'  F\u00f3rmula: Ib = S / ('+coefStr+' x V)\n'
+'  Ib = '+S_total.toFixed(2)+' / ('+coefStr+' x '+V+') => Ib = '+Ib.toFixed(2)+' A\n\n'
+'2. CAPACIDADE DE CONDU\u00c7\u00c3O CORRIGIDA (Iz)\n'
+'----------------------------------------------------------------------\n'
+'  Material : '+material.toUpperCase()+'   Isola\u00e7\u00e3o : '+isolacao.toUpperCase()+'\n'
+'  M\u00e9todo NBR 5410 : '+metodo.toUpperCase()+' ('+condC+' condutores carregados)\n'
+'  Se\u00e7\u00e3o avaliada : '+secaoSel+' mm\u00b2\n'
+'  Iz base (30\u00b0C) : '+resAtual.Iz_base.toFixed(2)+' A\n'
+'  Fator de temperatura ('+temp+'\u00b0C) : '+fTemp.toFixed(2)+'\n'
+'  Fator de agrupamento ('+agrup+' circ.) : '+fAgrup.toFixed(2)+'\n\n'
+'  F\u00f3rmula: Iz = Iz_base x Ftemp x Fagrup\n'
+'  Iz = '+resAtual.Iz_base.toFixed(2)+' x '+fTemp.toFixed(2)+' x '+fAgrup.toFixed(2)+' => Iz = '+resAtual.Iz_corrigida.toFixed(2)+' A\n\n'
+'3. QUEDA DE TENS\u00c3O (\u0394V)\n'
+'----------------------------------------------------------------------\n'
+'  Comprimento L = '+dist+' m\n'
+'  Resistividade \u03c1 ('+(material==='cu'?'Cobre':'Alum\u00ednio')+') = '+(material==='cu'?'0,021':'0,035')+' \u03a9.mm\u00b2/m\n\n'
+'  F\u00f3rmula: \u0394V = (coef x L x Ib x \u03c1) / S\n'
+'  \u0394V = ('+coefStr+' x '+dist+' x '+Ib.toFixed(2)+' x '+(material==='cu'?'0,021':'0,035')+') / '+secaoSel+'\n'
+'  \u0394V = '+resAtual.deltaV.toFixed(2)+' V => \u0394V% = '+resAtual.deltaVPercent.toFixed(2)+'%\n\n'
+'4. VERIFICA\u00c7\u00c3O FINAL \u2014 CRIT\u00c9RIOS NBR 5410\n'
+'----------------------------------------------------------------------\n'
+'  [Crit. 1] Iz ('+resAtual.Iz_corrigida.toFixed(2)+' A) >= Ib ('+Ib.toFixed(2)+' A): '+(resAtual.atendeCorrente?'APROVADO':'REPROVADO')+'\n'
+'  [Crit. 2] \u0394V% ('+resAtual.deltaVPercent.toFixed(2)+'%) <= 4,00%: '+(resAtual.atendeQueda?'APROVADO':'REPROVADO')+'\n\n'
+'  RESULTADO GERAL: '+(resAtual.atendeGeral?'ATENDE \u00c0 NBR 5410':'N\u00c3O ATENDE \u00c0 NBR 5410')+'\n\n'
+'----------------------------------------------------------------------\n'
+parecerGlobal+'\n'
+'======================================================================';

  document.getElementById('memoriaContent').textContent=memoriaGlobal;
}

/* =====================================================================
   ACCORDION E PDF
   ===================================================================== */
function toggleMemoria(){
  var c=document.getElementById('memoriaContent'),a=document.getElementById('accordionArrow');
  if(c.classList.contains('show')){c.classList.remove('show');a.innerHTML='&#9660;';}
  else{c.classList.add('show');a.innerHTML='&#9650;';}
}

function gerarPDF(){
  var dataHoje=new Date().toLocaleDateString('pt-BR');
  var bgB64=document.getElementById('bgBase64Store').value;
  // Captura o HTML do parecer exatamente como exibido no app
  var parecerHTML=document.getElementById('parecerTexto').innerHTML;
  var parecerAtende=document.getElementById('parecerCard').classList.contains('atende');
  var win=window.open('','_blank');
  var h='<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">'
    +'<title>Relat\u00f3rio Pr\u00e9-Dimensionamento El\u00e9trico NBR 5410</title>'
    +'<style>@page{size:A4;margin:15mm}'
    +'body{font-family:"Segoe UI",Arial,sans-serif;color:#0f172a;line-height:1.6;position:relative;background:#fff}'
    +'body::before{content:"";position:fixed;inset:0;background-image:url("data:image/jpeg;base64,'+bgB64+'");background-size:cover;opacity:0.05;z-index:-1}'
    +'.hdr{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #3b82f6;padding-bottom:12px;margin-bottom:20px}'
    +'.ttl{font-size:1.4rem;font-weight:bold;color:#1e3a8a}'
    +'.sub{font-size:.85rem;color:#475569}'
    +'.st{font-size:1.05rem;font-weight:bold;color:#1e293b;border-bottom:1px solid #cbd5e1;padding-bottom:4px;margin:18px 0 10px}'
    /* Parecer — visual idêntico ao app */
    +'.pb-atende{background:#f0fdf4;border:1px solid #86efac;border-radius:10px;padding:16px 18px;margin-bottom:16px;font-size:.9rem;line-height:1.7;color:#14532d}'
    +'.pb-reprov{background:#fef2f2;border:1px solid #fca5a5;border-radius:10px;padding:16px 18px;margin-bottom:16px;font-size:.9rem;line-height:1.7;color:#7f1d1d}'
    +'.parecer-aprovado-destaque{background:#dcfce7;border:2px solid #16a34a;border-radius:10px;padding:14px 18px;margin-top:12px;text-align:center;font-size:1.05rem;font-weight:700;color:#15803d;letter-spacing:.5px}'
    +'pre{background:#f1f5f9;padding:14px;font-family:Consolas,"Courier New",monospace;font-size:.78rem;white-space:pre-wrap;border-radius:6px;border:1px solid #e2e8f0}'
    +'.ftr{margin-top:30px;border-top:1px solid #cbd5e1;padding-top:10px;font-size:.75rem;color:#64748b;display:flex;justify-content:space-between}'
    +'</style></head><body>'
    +'<div class="hdr"><div><div class="ttl">&#9889; RELAT\u00d3RIO DE PR\u00c9-DIMENSIONAMENTO EL\u00c9TRICO</div>'
    +'<div class="sub">Em conformidade com a ABNT NBR 5410:2004</div></div>'
    +'<div style="text-align:right;font-size:.85rem;font-weight:bold;color:#3b82f6">EMISS\u00c3O: '+dataHoje+'</div></div>'
    +'<div class="st">1. Parecer T\u00e9cnico</div>'
    +'<div class="'+(parecerAtende?'pb-atende':'pb-reprov')+'">'+parecerHTML+'</div>'
    +'<div class="st">2. Mem\u00f3ria de C\u00e1lculo Detalhada</div>'
    +'<pre>'+memoriaGlobal+'</pre>'
    +'<div class="ftr">'
    +'<div>Aviso: este documento \u00e9 um pr\u00e9-dimensionamento e n\u00e3o substitui projeto el\u00e9trico elaborado por Engenheiro habilitado.</div>'
    +'<div>Data: '+dataHoje+'</div></div>'
    +'<script>window.onload=function(){window.print();}<\/script>'
    +'</body></html>';
  win.document.write(h);
  win.document.close();
}

/* =====================================================================
   LIMPAR E INICIALIZAR
   ===================================================================== */
function limpar(){
  cargas=[];contadorId=1;
  document.getElementById('distancia').value=30;
  document.getElementById('tensao').value=220;
  document.getElementById('secaoSelecionada').value=2.5;
  setFases('mono');
  adicionarCarga('Motor Bomba de \u00c1gua','motor','potencia',5,'CV',0.85,90,1);
  resetCalculado();
}

adicionarCarga('Motor Bomba de \u00c1gua','motor','potencia',5,'CV',0.85,90,1);
</script>

<input type="hidden" id="bgBase64Store" value="__BG__">
</body>
</html>"""

HTML_FINAL = HTML.replace('__BG__', BG_B64)

DEST = os.path.join(PASTA, "dimensionamento_eletrico.html")
with open(DEST, "w", encoding="utf-8") as f:
    f.write(HTML_FINAL)

print("Arquivo gerado: " + DEST)
print("Tamanho: {:,} bytes".format(os.path.getsize(DEST)))

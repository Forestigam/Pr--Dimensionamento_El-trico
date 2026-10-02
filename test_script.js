
/* ==========================================================================
   DADOS TÉCNICOS DA NBR 5410 E ARQUITETURA DO APLICATIVO
   ========================================================================== */

const TABELA_CAPACIDADE_CONDUCAO = {
  cu: {
    pvc: {
      b1: { 2: { 1.5: 17.5, 2.5: 24, 4: 32, 6: 41, 10: 57, 16: 76, 25: 101, 35: 125, 50: 151, 70: 192, 95: 232, 120: 269, 150: 300, 185: 341, 240: 400 }, 3: { 1.5: 15.5, 2.5: 21, 4: 28, 6: 36, 10: 50, 16: 68, 25: 89, 35: 110, 50: 134, 70: 171, 95: 207, 120: 239, 150: 267, 185: 303, 240: 356 } },
      b2: { 2: { 1.5: 16.5, 2.5: 23, 4: 30, 6: 38, 10: 52, 16: 69, 25: 90, 35: 111, 50: 133, 70: 168, 95: 201, 120: 232, 150: 258, 185: 294, 240: 344 }, 3: { 1.5: 15.0, 2.5: 20, 4: 27, 6: 34, 10: 46, 16: 62, 25: 80, 35: 99, 50: 118, 70: 149, 95: 179, 120: 206, 150: 225, 185: 258, 240: 301 } },
      c:  { 2: { 1.5: 19.5, 2.5: 27, 4: 36, 6: 46, 10: 63, 16: 85, 25: 112, 35: 138, 50: 168, 70: 213, 95: 258, 120: 299, 150: 344, 185: 392, 240: 461 }, 3: { 1.5: 17.5, 2.5: 24, 4: 32, 6: 41, 10: 57, 16: 76, 25: 96, 35: 119, 50: 144, 70: 184, 95: 223, 120: 259, 150: 299, 185: 341, 240: 403 } },
      d:  { 2: { 1.5: 22.0, 2.5: 29, 4: 38, 6: 47, 10: 63, 16: 81, 25: 104, 35: 125, 50: 148, 70: 180, 95: 214, 120: 243, 150: 273, 185: 308, 240: 356 }, 3: { 1.5: 18.0, 2.5: 24, 4: 31, 6: 39, 10: 52, 16: 67, 25: 86, 35: 103, 50: 122, 70: 149, 95: 177, 120: 201, 150: 226, 185: 255, 240: 295 } }
    },
    xlpe_epr: {
      b1: { 2: { 1.5: 22, 2.5: 31, 4: 42, 6: 54, 10: 75, 16: 100, 25: 133, 35: 164, 50: 198, 70: 253, 95: 306, 120: 354, 150: 393, 185: 449, 240: 528 }, 3: { 1.5: 19, 2.5: 27, 4: 37, 6: 48, 10: 66, 16: 89, 25: 117, 35: 144, 50: 175, 70: 224, 95: 271, 120: 314, 150: 349, 185: 398, 240: 468 } },
      b2: { 2: { 1.5: 21, 2.5: 29, 4: 39, 6: 50, 10: 68, 16: 91, 25: 119, 35: 146, 50: 175, 70: 221, 95: 265, 120: 305, 150: 339, 185: 386, 240: 452 }, 3: { 1.5: 18.5, 2.5: 26, 4: 35, 6: 44, 10: 60, 16: 80, 25: 105, 35: 129, 50: 154, 70: 194, 95: 233, 120: 268, 150: 297, 185: 338, 240: 394 } },
      c:  { 2: { 1.5: 26, 2.5: 36, 4: 49, 6: 63, 10: 86, 16: 115, 25: 149, 35: 185, 50: 225, 70: 286, 95: 347, 120: 401, 150: 462, 185: 527, 240: 619 }, 3: { 1.5: 23, 2.5: 32, 4: 43, 6: 55, 10: 75, 16: 100, 25: 127, 35: 158, 50: 192, 70: 246, 95: 298, 120: 346, 150: 399, 185: 456, 240: 538 } },
      d:  { 2: { 1.5: 26, 2.5: 35, 4: 45, 6: 55, 10: 74, 16: 96, 25: 123, 35: 147, 50: 174, 70: 211, 95: 250, 120: 283, 150: 317, 185: 357, 240: 409 }, 3: { 1.5: 22, 2.5: 29, 4: 37, 6: 46, 10: 61, 16: 79, 25: 101, 35: 121, 50: 143, 70: 174, 95: 206, 120: 234, 150: 262, 185: 294, 240: 338 } }
    }
  },
  al: {
    pvc: {
      b1: { 2: { 16: 59, 25: 78, 35: 96, 50: 117, 70: 148, 95: 180, 120: 208, 150: 232, 185: 264, 240: 310 }, 3: { 16: 52, 25: 69, 35: 85, 50: 103, 70: 131, 95: 160, 120: 185, 150: 206, 185: 235, 240: 275 } },
      b2: { 2: { 16: 53, 25: 70, 35: 86, 50: 103, 70: 130, 95: 156, 120: 180, 150: 200, 185: 228, 240: 267 }, 3: { 16: 47, 25: 62, 35: 76, 50: 91, 70: 115, 95: 138, 120: 159, 150: 174, 185: 199, 240: 233 } },
      c:  { 2: { 16: 66, 25: 87, 35: 107, 50: 131, 70: 166, 95: 201, 120: 233, 150: 268, 185: 306, 240: 360 }, 3: { 16: 59, 25: 75, 35: 93, 50: 113, 70: 144, 95: 175, 120: 203, 150: 234, 185: 267, 240: 316 } },
      d:  { 2: { 16: 63, 25: 81, 35: 97, 50: 115, 70: 140, 95: 166, 120: 189, 150: 212, 185: 239, 240: 276 }, 3: { 16: 52, 25: 67, 35: 80, 50: 95, 70: 115, 95: 137, 120: 156, 150: 175, 185: 197, 240: 228 } }
    },
    xlpe_epr: {
      b1: { 2: { 16: 78, 25: 103, 35: 127, 50: 154, 70: 197, 95: 238, 120: 275, 150: 306, 185: 349, 240: 411 }, 3: { 16: 69, 25: 91, 35: 112, 50: 136, 70: 174, 95: 211, 120: 244, 150: 271, 185: 309, 240: 364 } },
      b2: { 2: { 16: 71, 25: 92, 35: 113, 50: 136, 70: 172, 95: 206, 120: 237, 150: 263, 185: 300, 240: 351 }, 3: { 16: 62, 25: 81, 35: 100, 50: 120, 70: 151, 95: 181, 120: 208, 150: 231, 185: 263, 240: 307 } },
      c:  { 2: { 16: 89, 25: 116, 35: 144, 50: 175, 70: 223, 95: 270, 120: 312, 150: 359, 185: 410, 240: 482 }, 3: { 16: 78, 25: 99, 35: 123, 50: 150, 70: 192, 95: 232, 120: 269, 150: 310, 185: 355, 240: 419 } },
      d:  { 2: { 16: 75, 25: 96, 35: 114, 50: 135, 70: 164, 95: 194, 120: 220, 150: 246, 185: 277, 240: 318 }, 3: { 16: 62, 25: 79, 35: 94, 50: 111, 70: 135, 95: 160, 120: 182, 150: 203, 185: 228, 240: 262 } }
    }
  }
};

const FATORES_TEMPERATURA = {
  pvc: { 30: 1.00, 35: 0.94, 40: 0.87, 45: 0.79, 50: 0.71 },
  xlpe_epr: { 30: 1.00, 35: 0.96, 40: 0.91, 45: 0.87, 50: 0.82 }
};

const FATORES_AGRUPAMENTO = {
  1: 1.00, 2: 0.80, 3: 0.70, 4: 0.65, 5: 0.60, 6: 0.57, 7: 0.54, 8: 0.50
};

const DIAMETRO_CONDUTOR_APROX = {
  1.5: "1,38 mm", 2.5: "1,78 mm", 4: "2,26 mm", 6: "2,76 mm", 10: "3,57 mm",
  16: "4,51 mm", 25: "5,64 mm", 35: "6,68 mm", 50: "7,98 mm", 70: "9,44 mm",
  95: "11,00 mm", 120: "12,36 mm", 150: "13,82 mm", 185: "15,35 mm", 240: "17,48 mm"
};

const SECOES_COMERCIAIS = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240];

let estadoFases = 'mono';
let cargas = [];
let memoriaCalculoGlobal = "";

// Inicialização ao carregar a página
window.addEventListener('DOMContentLoaded', () => {
  adicionarCarga("Motor Bomba de Água", "motor", "potencia", 5, "HP", 0.85, 80, 1);
  renderizarCardsCargas();
});

function setFases(fase) {
  estadoFases = fase;
  document.getElementById('btnFaseMono').classList.toggle('active', fase === 'mono');
  document.getElementById('btnFaseBi').classList.toggle('active', fase === 'bi');
  document.getElementById('btnFaseTri').classList.toggle('active', fase === 'tri');
  resetCalculado();
}

function syncFP(val) {
  let num = parseFloat(val);
  if (isNaN(num)) num = 0.85;
  num = Math.max(0.15, Math.min(1.00, num));
  document.getElementById('fpGlobalRange').value = num;
  document.getElementById('fpGlobalNum').value = num.toFixed(2);
  resetCalculado();
}

function onMaterialChange() {
  const mat = document.getElementById('materialCondutor').value;
  const warn = document.getElementById('alWarning');
  if (mat === 'al') {
    warn.style.display = 'block';
  } else {
    warn.style.display = 'none';
  }
  resetCalculado();
}

function resetCalculado() {
  document.getElementById('containerResultados').style.display = 'none';
  document.getElementById('panelPlaceholder').style.display = 'flex';
}

function executarCalculoClique() {
  document.getElementById('panelPlaceholder').style.display = 'none';
  document.getElementById('containerResultados').style.display = 'flex';
  calcular();
}

/* ==========================================================================
   GERENCIAMENTO DE CARGAS DINÂMICAS
   ========================================================================== */

function adicionarCarga(nome = "", tipoCarga = "motor", modo = "potencia", valorPot = 1000, unidadePot = "W", fp = 0.85, rend = 80, qtd = 1) {
  const id = Date.now() + Math.random().toString(36).substr(2, 4);
  cargas.push({ id, nome, tipoCarga, modo, valorPot, unidadePot, correnteNom: 10, fp, rend, qtd });
  renderizarCardsCargas();
  resetCalculado();
}

function removerCarga(id) {
  if (cargas.length <= 1) {
    alert("O circuito deve conter pelo menos uma carga cadastrada.");
    return;
  }
  cargas = cargas.filter(c => c.id !== id);
  renderizarCardsCargas();
  resetCalculado();
}

function renderizarCardsCargas() {
  const container = document.getElementById('loadCardsContainer');
  container.innerHTML = "";

  cargas.forEach((carga, index) => {
    const card = document.createElement('div');
    card.className = 'load-card';
    card.innerHTML = `
      <div class="load-card-header">
        <span class="load-card-title">⚡ Carga #${index + 1}</span>
        ${cargas.length > 1 ? `<button type="button" class="btn-remove-load" onclick="removerCarga('${carga.id}')">🗑️ Remover</button>` : ''}
      </div>
      <div class="form-row">
        <div class="form-group" style="grid-column: span 2;">
          <label>Identificação / Nome da Carga</label>
          <input type="text" value="${carga.nome}" placeholder="Ex: Motor Bomba, Compressor, Iluminação" oninput="atualizarCarga('${carga.id}', 'nome', this.value);">
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label>Tipo de Carga</label>
          <select onchange="atualizarCarga('${carga.id}', 'tipoCarga', this.value);">
            <option value="motor" ${carga.tipoCarga === 'motor' ? 'selected' : ''}>Motor Elétrico</option>
            <option value="resistiva" ${carga.tipoCarga === 'resistiva' ? 'selected' : ''}>Carga Resistiva (Chuveiro, Aquecedor, Lâmpada Incand.)</option>
            <option value="nao_identificado" ${carga.tipoCarga === 'nao_identificado' ? 'selected' : ''}>Carga Geral / Não Identificado</option>
          </select>
        </div>
        <div class="form-group">
          <label>Modo de Especificação</label>
          <select onchange="atualizarCarga('${carga.id}', 'modo', this.value);">
            <option value="potencia" ${carga.modo === 'potencia' ? 'selected' : ''}>Usar Potência</option>
            <option value="corrente" ${carga.modo === 'corrente' ? 'selected' : ''}>Usar Corrente Nominal (A)</option>
          </select>
        </div>
      </div>
      <div class="form-row">
        ${carga.modo === 'potencia' ? `
          <div class="form-group">
            <label>Potência Nominal</label>
            <div style="display: flex; gap: 8px;">
              <input type="number" value="${carga.valorPot}" min="0.1" step="0.1" style="flex: 1;" oninput="atualizarCarga('${carga.id}', 'valorPot', parseFloat(this.value));">
              <select style="width: 85px;" onchange="atualizarCarga('${carga.id}', 'unidadePot', this.value);">
                <option value="W" ${carga.unidadePot === 'W' ? 'selected' : ''}>W</option>
                <option value="kW" ${carga.unidadePot === 'kW' ? 'selected' : ''}>kW</option>
                ${carga.tipoCarga === 'motor' ? `
                  <option value="CV" ${carga.unidadePot === 'CV' ? 'selected' : ''}>CV</option>
                  <option value="HP" ${carga.unidadePot === 'HP' ? 'selected' : ''}>HP</option>
                ` : ''}
              </select>
            </div>
          </div>
        ` : `
          <div class="form-group">
            <label>Corrente Nominal (A)</label>
            <input type="number" value="${carga.correnteNom}" min="0.1" step="0.1" oninput="atualizarCarga('${carga.id}', 'correnteNom', parseFloat(this.value));">
          </div>
        `}
        ${carga.tipoCarga === 'motor' ? `
          <div class="form-group">
            <label>Fator de Potência (cos φ)</label>
            <input type="number" value="${carga.fp}" min="0.15" max="1.00" step="0.01" oninput="atualizarCarga('${carga.id}', 'fp', parseFloat(this.value));">
          </div>
          ${carga.modo === 'potencia' ? `
            <div class="form-group">
              <label>Rendimento η (%)</label>
              <input type="number" value="${carga.rend}" min="10" max="100" step="1" oninput="atualizarCarga('${carga.id}', 'rend', parseFloat(this.value));">
            </div>
          ` : ''}
        ` : ''}
        <div class="form-group">
          <label>Quantidade (Qtd)</label>
          <input type="number" value="${carga.qtd}" min="1" step="1" oninput="atualizarCarga('${carga.id}', 'qtd', parseInt(this.value));">
        </div>
      </div>
    `;
    container.appendChild(card);
  });
}

function atualizarCarga(id, campo, valor) {
  const c = cargas.find(item => item.id === id);
  if (c) {
    c[campo] = valor;
    if (campo === 'tipoCarga' || campo === 'modo') {
      // Ajustar unidade se tipo alterou e tinha selecionado CV/HP
      if (c.tipoCarga !== 'motor' && (c.unidadePot === 'CV' || c.unidadePot === 'HP')) {
        c.unidadePot = 'kW';
      }
      renderizarCardsCargas();
    }
    resetCalculado();
  }
}

/* ==========================================================================
   MOTOR PRINCIPAL DE CÁLCULO E AUDITORIA NBR 5410
   ========================================================================== */

function calcular() {
  // 1. Obter Dados da Instalação
  const material = document.getElementById('materialCondutor').value;
  const isolacao = document.getElementById('isolacao').value;
  const V = parseFloat(document.getElementById('tensao').value) || 220;
  const distancia = parseFloat(document.getElementById('distancia').value) || 30;
  const fpGlobal = parseFloat(document.getElementById('fpGlobalNum').value) || 0.85;
  const metodo = document.getElementById('metodoInstalacao').value;
  
  // Condutores Carregados derivados de Fases
  const condCarregados = (estadoFases === 'tri') ? 3 : 2;
  
  const temp = document.getElementById('temperatura').value;
  const agrup = document.getElementById('agrupamento').value;
  const secaoSelecionada = parseFloat(document.getElementById('secaoSelecionada').value) || 2.5;

  // Atualizar Diâmetro Aproximado
  document.getElementById('diametroAprox').value = DIAMETRO_CONDUTOR_APROX[secaoSelecionada] || "N/D";

  // 2. Cálculo Vetorial de Cargas
  let P_total_W = 0;
  let Q_total_VAr = 0;

  const tabelaResumo = document.getElementById('tabelaResumoCargas');
  tabelaResumo.innerHTML = "";

  cargas.forEach((c, idx) => {
    let P_c = 0; // W
    let I_c = 0; // A
    let fp_c = 1.0;
    let rend_c = 1.0;

    if (c.tipoCarga === 'motor') {
      fp_c = Math.max(0.15, Math.min(1.00, c.fp || 0.85));
      rend_c = c.modo === 'potencia' ? ((c.rend || 80) / 100) : 1.0;
    } else if (c.tipoCarga === 'resistiva') {
      fp_c = 1.00;
      rend_c = 1.00;
    } else { // nao_identificado
      fp_c = fpGlobal;
      rend_c = 1.00;
    }

    let qtd_c = c.qtd || 1;
    let especificacaoStr = "";

    if (c.modo === 'potencia') {
      let valPot = c.valorPot || 0;
      let unidade = c.unidadePot || 'W';
      let factorWatts = 1;
      if (unidade === 'kW') factorWatts = 1000;
      else if (unidade === 'CV') factorWatts = 735.5;
      else if (unidade === 'HP') factorWatts = 745.7;

      let potUtilW = valPot * factorWatts;
      P_c = potUtilW * qtd_c;

      // Equação de Corrente conforme Número de Fases
      if (estadoFases === 'mono' || estadoFases === 'bi') {
        I_c = P_c / (V * fp_c * rend_c);
      } else { // tri
        I_c = P_c / (Math.sqrt(3) * V * fp_c * rend_c);
      }

      especificacaoStr = `${valPot.toLocaleString('pt-BR')} ${unidade} (${(P_c/1000).toLocaleString('pt-BR', {minimumFractionDigits: 2})} kW)`;
    } else { // corrente nominal informada
      I_c = (c.correnteNom || 0) * qtd_c;
      if (estadoFases === 'tri') {
        P_c = Math.sqrt(3) * V * I_c * fp_c;
      } else {
        P_c = V * I_c * fp_c;
      }
      especificacaoStr = `CorrenteNom: ${I_c.toLocaleString('pt-BR', {minimumFractionDigits: 2})} A`;
    }

    let phi = Math.acos(fp_c);
    let Q_c = P_c * Math.tan(phi);

    P_total_W += P_c;
    Q_total_VAr += Q_c;

    let tipoRotulo = c.tipoCarga === 'motor' ? 'Motor' : c.tipoCarga === 'resistiva' ? 'Resistiva' : 'Geral';

    // Adiciona linha na tabela de resumo
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${c.nome || `Carga #${idx+1}`}</td>
      <td>${tipoRotulo}</td>
      <td>${especificacaoStr}</td>
      <td style="text-align: right;">${I_c.toLocaleString('pt-BR', {minimumFractionDigits: 2})} A</td>
      <td style="text-align: right;">${fp_c.toFixed(2)}</td>
      <td style="text-align: right;">${c.tipoCarga === 'motor' && c.modo === 'potencia' ? `${(c.rend || 80)}%` : '-'}</td>
      <td style="text-align: center;">${qtd_c}</td>
    `;
    tabelaResumo.appendChild(tr);
  });

  // Potência Aparente Total e Fator de Potência Equivalente
  let S_total_VA = Math.sqrt(Math.pow(P_total_W, 2) + Math.pow(Q_total_VAr, 2));
  let fp_equivalente = S_total_VA > 0 ? P_total_W / S_total_VA : 1.0;

  // Corrente de Projeto Total Ib (A)
  let Ib = 0;
  if (estadoFases === 'mono' || estadoFases === 'bi') {
    Ib = S_total_VA / V;
  } else { // tri
    Ib = S_total_VA / (Math.sqrt(3) * V);
  }

  // 3. Fatores de Correção NBR 5410
  const fTemp = FATORES_TEMPERATURA[isolacao][temp] || 1.0;
  const fAgrup = FATORES_AGRUPAMENTO[agrup] || 1.0;
  const fTotal = fTemp * fAgrup;

  // Function helper para calcular capacidade e queda de tensão para uma seção específica
  function avaliarSecao(secao) {
    let tabMat = TABELA_CAPACIDADE_CONDUCAO[material];
    let tabIso = tabMat ? tabMat[isolacao] : null;
    let tabMet = tabIso ? tabIso[metodo] : null;
    let tabCond = tabMet ? tabMet[condCarregados] : null;
    let Iz_base = tabCond && tabCond[secao] ? tabCond[secao] : 0;

    let Iz_corrigida = Iz_base * fTotal;

    let rho = material === 'cu' ? 0.021 : 0.035;
    let x = 0.00008; // Reatância indutiva Ohm/m
    let cosPhi = fp_equivalente;
    let sinPhi = Math.sin(Math.acos(cosPhi));

    let deltaV = 0;
    if (estadoFases === 'mono' || estadoFases === 'bi') {
      deltaV = (2 * distancia * Ib * (rho * cosPhi + (x * secao * sinPhi))) / secao;
    } else { // tri
      deltaV = (Math.sqrt(3) * distancia * Ib * (rho * cosPhi + (x * secao * sinPhi))) / secao;
    }

    let deltaVPercent = (deltaV / V) * 100;
    let atendeCorrente = Iz_corrigida >= Ib && Iz_base > 0;
    let atendeQueda = deltaVPercent <= 4.00;
    let atendeGeral = atendeCorrente && atendeQueda;

    return {
      secao,
      Iz_base,
      Iz_corrigida,
      deltaV,
      deltaVPercent,
      atendeCorrente,
      atendeQueda,
      atendeGeral
    };
  }

  // Avaliação da Seção Selecionada pelo Usuário
  const resSecaoSel = avaliarSecao(secaoSelecionada);

  // 4. Teste Automático de Bitolas Superiores (Sugestão de Menor Bitola)
  let secaoSugerida = null;
  for (let s of SECOES_COMERCIAIS) {
    if (material === 'al' && s < 16) continue;
    let res = avaliarSecao(s);
    if (res.atendeGeral) {
      secaoSugerida = res;
      break;
    }
  }

  // 5. Atualizar Métricas na Tela
  document.getElementById('resIb').innerText = Ib.toLocaleString('pt-BR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + " A";
  document.getElementById('resIz').innerText = resSecaoSel.Iz_corrigida.toLocaleString('pt-BR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + " A";
  document.getElementById('resVsaida').innerText = (V - resSecaoSel.deltaV).toLocaleString('pt-BR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + " V";
  document.getElementById('resDeltaV').innerText = resSecaoSel.deltaV.toLocaleString('pt-BR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + " V";
  document.getElementById('resDeltaVPercent').innerText = resSecaoSel.deltaVPercent.toLocaleString('pt-BR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + " %";

  // 6. Atualizar Badge de Resultado e Parecer Técnico Unificado
  const badge = document.getElementById('resultBadge');
  const icon = document.getElementById('resultIcon');
  const title = document.getElementById('resultTitle');
  const sub = document.getElementById('resultSub');
  const parecerCard = document.getElementById('parecerCard');
  const parecerTexto = document.getElementById('parecerTexto');

  if (material === 'al' && secaoSelecionada < 16) {
    badge.className = "result-badge nao-atende";
    icon.innerText = "🔴";
    title.innerText = "CONDUTOR NÃO PERMITIDO";
    sub.innerText = "Uso de alumínio em seções < 16 mm² é vetado pela NBR 5410.";
    parecerCard.className = "parecer-card nao-atende";
    parecerTexto.innerHTML = `🔴 <strong>PARECER TÉCNICO & NORMATIVO:</strong><br>A norma ABNT NBR 5410 proíbe condutores de alumínio com seção nominal inferior a 16 mm² para instalações prediais de baixa tensão.<br><br>📍 <strong>RECOMENDAÇÃO:</strong> Utilize condutores de Cobre ou altere a seção para no mínimo <strong>16 mm²</strong> para Alumínio.`;
  } else if (resSecaoSel.atendeGeral) {
    badge.className = "result-badge atende";
    icon.innerText = "🟢";
    title.innerText = "ATENDE À NBR 5410";
    sub.innerText = "Capacidade de condução e Queda de Tensão dentro dos limites.";
    parecerCard.className = "parecer-card atende";
    parecerTexto.innerHTML = `🟢 <strong>PARECER TÉCNICO & DIMENSIONAMENTO:</strong><br>Os parâmetros informados com a seção selecionada de <strong>${secaoSelecionada.toLocaleString('pt-BR')} mm²</strong> apresentam capacidade de condução de corrente (${resSecaoSel.Iz_corrigida.toFixed(2)} A ≥ ${Ib.toFixed(2)} A) e queda de tensão (${resSecaoSel.deltaVPercent.toFixed(2)}% ≤ 4,00%) totalmente conformes com os critérios da ABNT NBR 5410.<br><br>📍 <strong>SEÇÃO RECOMENDADA:</strong> <strong>${secaoSelecionada.toLocaleString('pt-BR')} mm²</strong>`;
  } else {
    badge.className = "result-badge nao-atende";
    icon.innerText = "🔴";
    title.innerText = "NÃO ATENDE AOS CRITÉRIOS";
    sub.innerText = "Condutor insuficiente para os parâmetros informados.";
    parecerCard.className = "parecer-card nao-atende";

    let diag = [];
    if (!resSecaoSel.atendeCorrente) {
      diag.push(`• ⚡ <strong>Capacidade de Condução Insuficiente:</strong> Corrente Ib = ${Ib.toFixed(2)} A supera a capacidade corrigida Iz = ${resSecaoSel.Iz_corrigida.toFixed(2)} A.`);
    }
    if (!resSecaoSel.atendeQueda) {
      diag.push(`• 📉 <strong>Queda de Tensão Excessiva:</strong> Queda calculada = ${resSecaoSel.deltaVPercent.toFixed(2)}% (limite 4,00%). Queda: ${resSecaoSel.deltaV.toFixed(2)} V.`);
    }

    let recomendacao = "";
    if (secaoSugerida) {
      recomendacao = `<br><br>📍 <strong>SEÇÃO RECOMENDADA:</strong> Recomenda-se utilizar a seção de <strong>${secaoSugerida.secao.toLocaleString('pt-BR')} mm²</strong>, que é a primeira bitola comercial que satisfaz simultaneamente à capacidade de corrente (Iz = ${secaoSugerida.Iz_corrigida.toFixed(2)} A) e à queda de tensão (ΔV% = ${secaoSugerida.deltaVPercent.toFixed(2)}%).`;
    } else {
      recomendacao = `<br><br>⚠️ <strong>SOBRECARGA CRÍTICA:</strong> Nenhuma bitola comercial até 240 mm² atendeu. Recomenda-se subdividir o circuito ou elevar a tensão.`;
    }

    parecerTexto.innerHTML = `🔴 <strong>PARECER TÉCNICO & DIAGNÓSTICO:</strong><br>${diag.join('<br>')}${recomendacao}`;
  }

  // 7. Renderizar Tabela Comparativa (Apenas 2 cabos antes e 2 depois do recomendado/selecionado)
  const tbodyComp = document.getElementById('tabelaBitolasComp');
  tbodyComp.innerHTML = "";

  let secaoRef = secaoSugerida ? secaoSugerida.secao : secaoSelecionada;
  let idxRef = SECOES_COMERCIAIS.indexOf(secaoRef);
  if (idxRef === -1) idxRef = SECOES_COMERCIAIS.indexOf(secaoSelecionada);

  let startIdx = Math.max(0, idxRef - 2);
  let endIdx = Math.min(SECOES_COMERCIAIS.length - 1, idxRef + 2);
  let secoesFiltradas = SECOES_COMERCIAIS.slice(startIdx, endIdx + 1);

  secoesFiltradas.forEach(s => {
    if (material === 'al' && s < 16) return;
    let evalS = avaliarSecao(s);
    let isSelected = s === secaoSelecionada;
    let isSuggested = secaoSugerida && s === secaoSugerida.secao;

    const tr = document.createElement('tr');
    if (isSuggested || (isSelected && evalS.atendeGeral)) tr.className = "highlight-suggest";

    tr.innerHTML = `
      <td><strong>${s.toLocaleString('pt-BR')} mm²</strong> ${isSelected ? '📌 <i>(Atual)</i>' : ''} ${isSuggested ? '⭐ <i>(Recomendada)</i>' : ''}</td>
      <td>${evalS.Iz_corrigida.toFixed(2)} A</td>
      <td>${Ib.toFixed(2)} A</td>
      <td>${evalS.deltaV.toFixed(2)} V</td>
      <td>${evalS.deltaVPercent.toFixed(2)} %</td>
      <td>${evalS.atendeGeral ? '🟢 ✅ OK' : '🔴 ❌ Reprovado'}</td>
    `;
    tbodyComp.appendChild(tr);
  });

  // 8. Gerar Memória de Cálculo Detalhada
  const memoriaContent = document.getElementById('memoriaContent');
  memoriaCalculoGlobal = 
`======================================================================
                  MEMÓRIA DE CÁLCULO PASSO A PASSO
======================================================================

1. CÁLCULO DA POTÊNCIA E CORRENTE DE PROJETO (Ib):
----------------------------------------------------------------------
• Potência Ativa Total (P): ${(P_total_W / 1000).toFixed(2)} kW (${P_total_W.toFixed(0)} W)
• Potência Reativa Total (Q): ${(Q_total_VAr / 1000).toFixed(2)} kVAR
• Potência Aparente Total (S): ${(S_total_VA / 1000).toFixed(2)} kVA
• Fator de Potência Equivalente (FPeq): ${fp_equivalente.toFixed(4)}
• Sistema Elétrico: ${estadoFases === 'mono' ? 'Monofásico (1F)' : estadoFases === 'bi' ? 'Bifásico (2F)' : 'Trifásico (3F)'} - ${V} V

Fórmula da Corrente de Projeto (Ib):
${estadoFases === 'tri' ? 'Ib = S / (√3 × V)' : 'Ib = S / V'}
Ib = ${S_total_VA.toFixed(2)} / (${estadoFases === 'tri' ? `1,73205 × ${V}` : `${V}`})
=> Ib = ${Ib.toFixed(2)} A

2. CAPACIDADE DE CONDUÇÃO DE CORRENTE (Iz Corrigida):
----------------------------------------------------------------------
• Material: ${material.toUpperCase()} | Isolação: ${isolacao.toUpperCase()}
• Método de Instalação NBR 5410: ${metodo.toUpperCase()} (${condCarregados} condutores carregados)
• Seção do Condutor Avaliada: ${secaoSelecionada} mm²
• Iz Base (Tabela NBR 5410 a 30°C): ${resSecaoSel.Iz_base.toFixed(2)} A
• Fator de Temperatura (${temp}°C): ${fTemp.toFixed(2)}
• Fator de Agrupamento (${agrup} circ.): ${fAgrup.toFixed(2)}
• Fator de Correção Total: ${fTotal.toFixed(4)}

Fórmula: Iz_corrigida = Iz_base × Ftemp × Fagrup
Iz_corrigida = ${resSecaoSel.Iz_base.toFixed(2)} × ${fTemp.toFixed(2)} × ${fAgrup.toFixed(2)}
=> Iz_corrigida = ${resSecaoSel.Iz_corrigida.toFixed(2)} A

3. QUEDA DE TENSÃO (ΔV):
----------------------------------------------------------------------
• Distância (L): ${distancia} m
• Resistividade do ${material === 'cu' ? 'Cobre' : 'Alumínio'} (ρ): ${material === 'cu' ? '0,021' : '0,035'} Ω.mm²/m

Fórmula da Queda de Tensão (ΔV):
${estadoFases === 'tri' ? 'ΔV = (√3 × L × Ib × (ρ × cosφ + x × S × sinφ)) / S' : 'ΔV = (2 × L × Ib × (ρ × cosφ + x × S × sinφ)) / S'}
ΔV calculada: ${resSecaoSel.deltaV.toFixed(2)} V
Porcentagem de queda: ΔV% = (${resSecaoSel.deltaV.toFixed(2)} / ${V}) × 100 = ${resSecaoSel.deltaVPercent.toFixed(2)} %

4. VERIFICAÇÃO FINAL DOS CRITÉRIOS NBR 5410:
----------------------------------------------------------------------
[Critério 1] Capacidade de Condução: Ib (${Ib.toFixed(2)} A) ≤ Iz_corrigida (${resSecaoSel.Iz_corrigida.toFixed(2)} A)
Result: ${resSecaoSel.atendeCorrente ? '✅ APROVADO' : '❌ REPROVADO'}

[Critério 2] Queda de Tensão: ΔV% (${resSecaoSel.deltaVPercent.toFixed(2)}%) ≤ 4,00%
Result: ${resSecaoSel.atendeQueda ? '✅ APROVADO' : '❌ REPROVADO'}

SITUAÇÃO GERAL: ${resSecaoSel.atendeGeral ? '🟢 ATENDE À NBR 5410' : '🔴 NÃO ATENDE À NBR 5410'}
======================================================================`;

  memoriaContent.innerText = memoriaCalculoGlobal;
}

function toggleMemoria() {
  const content = document.getElementById('memoriaContent');
  const arrow = document.getElementById('accordionArrow');
  if (content.classList.contains('show')) {
    content.classList.remove('show');
    arrow.innerText = '▼';
  } else {
    content.classList.add('show');
    arrow.innerText = '▲';
  }
}

function gerarPDF() {
  const dataHoje = new Date().toLocaleDateString('pt-BR');
  const parecerHTML = document.getElementById('parecerTexto').innerHTML;

  const win = window.open('', '_blank');
  win.document.write(`
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
      <meta charset="UTF-8">
      <title>Relatório de Dimensionamento Elétrico — NBR 5410</title>
      <style>
        @page { size: A4; margin: 15mm; }
        body {
          font-family: 'Segoe UI', Arial, sans-serif;
          color: #0f172a;
          line-height: 1.5;
          position: relative;
          background: #ffffff;
        }
        body::before {
          content: "";
          position: fixed;
          inset: 0;
          background-image: url('data:image/jpeg;base64,${bg_base64}');
          background-size: cover;
          background-position: center;
          opacity: 0.05;
          z-index: -1;
        }
        .header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          border-bottom: 2px solid #3b82f6;
          padding-bottom: 12px;
          margin-bottom: 20px;
        }
        .title { font-size: 1.4rem; font-weight: bold; color: #1e3a8a; }
        .subtitle { font-size: 0.85rem; color: #475569; }
        .section-title {
          font-size: 1.05rem;
          font-weight: bold;
          color: #1e293b;
          border-bottom: 1px solid #cbd5e1;
          padding-bottom: 4px;
          margin-top: 18px;
          margin-bottom: 10px;
        }
        .parecer-box {
          background: #f8fafc;
          border-left: 4px solid #3b82f6;
          padding: 12px;
          margin-bottom: 16px;
          font-size: 0.9rem;
        }
        pre {
          background: #f1f5f9;
          padding: 12px;
          font-family: 'Consolas', 'Courier New', monospace;
          font-size: 0.8rem;
          white-space: pre-wrap;
          border-radius: 6px;
          border: 1px solid #e2e8f0;
        }
        .footer {
          margin-top: 30px;
          border-top: 1px solid #cbd5e1;
          padding-top: 10px;
          font-size: 0.75rem;
          color: #64748b;
          display: flex;
          justify-content: space-between;
        }
      </style>
    </head>
    <body>
      <div class="header">
        <div>
          <div class="title">⚡ RELATÓRIO DE PRÉ-DIMENSIONAMENTO ELÉTRICO</div>
          <div class="subtitle">Em conformidade com a ABNT NBR 5410:2004</div>
        </div>
        <div style="text-align: right; font-size: 0.85rem; font-weight: bold; color: #3b82f6;">
          EMISSÃO: ${dataHoje}
        </div>
      </div>

      <div class="section-title">1. Parecer Técnico & Recomendação</div>
      <div class="parecer-box">
        ${parecerHTML}
      </div>

      <div class="section-title">2. Memória de Cálculo Detalhada Passo a Passo</div>
      <pre>${memoriaCalculoGlobal}</pre>

      <div class="footer">
        <div>Aviso: Este documento de pré-dimensionamento não substitui o projeto elétrico definitivo elaborado por Engenheiro Elétrico habilitado.</div>
        <div>Data: ${dataHoje}</div>
      </div>

      <script>
        window.onload = function() { window.print(); }
      </script>
    </body>
    </html>
  `);
  win.document.close();
}

function limpar() {
  cargas = [];
  document.getElementById('distancia').value = 30;
  document.getElementById('tensao').value = 220;
  setFases('mono');
  document.getElementById('secaoSelecionada').value = 2.5;
  adicionarCarga("Carga Exemplo", "motor", "potencia", 1, "kW", 0.85, 80, 1);
  resetCalculado();
}

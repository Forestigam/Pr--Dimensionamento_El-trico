import os

file_path = r"C:\Users\Edimar\.gemini\antigravity\scratch\Queda de tensão em Cabo - NBR 5410\create_app.py"
log_path = r"C:\Users\Edimar\.gemini\antigravity\brain\e4f1c78c-fcf8-4a8a-a0af-b080a8242099\.system_generated\tasks\task-776.log"

with open(log_path, 'r', encoding='utf-8') as f:
    tabela_line = f.readlines()[0].strip()

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

# 1. Replace TABELA definition
# Find from `var TABELA={` to `};`
tabela_pattern = re.compile(r'var TABELA=\{.*?\};', re.DOTALL)
content = tabela_pattern.sub(tabela_line, content)

# 2. Replace DIAM
diam_old = r'var DIAM={1.5:"1,38 mm",2.5:"1,78 mm",4:"2,26 mm",6:"2,76 mm",10:"3,57 mm",16:"4,51 mm",25:"5,64 mm",35:"6,68 mm",50:"7,98 mm",70:"9,44 mm",95:"11,00 mm",120:"12,36 mm",150:"13,82 mm",185:"15,35 mm",240:"17,48 mm"};'
diam_new = r'var DIAM={1.5:"1,38 mm",2.5:"1,78 mm",4:"2,26 mm",6:"2,76 mm",10:"3,57 mm",16:"4,51 mm",25:"5,64 mm",35:"6,68 mm",50:"7,98 mm",70:"9,44 mm",95:"11,00 mm",120:"12,36 mm",150:"13,82 mm",185:"15,35 mm",240:"17,48 mm",300:"19,50 mm",400:"22,50 mm",500:"25,20 mm"};'
content = content.replace(diam_old, diam_new)

# 3. Replace SECOES
secoes_old = r'var SECOES=[1.5,2.5,4,6,10,16,25,35,50,70,95,120,150,185,240];'
secoes_new = r'var SECOES=[1.5,2.5,4,6,10,16,25,35,50,70,95,120,150,185,240,300,400,500];'
content = content.replace(secoes_old, secoes_new)

# 4. Update secaoSelecionada HTML
sec_html_old = r'<option value="240">240,0 mm²</option>'
sec_html_new = r'<option value="240">240,0 mm²</option>\n          <option value="300">300,0 mm²</option>\n          <option value="400">400,0 mm²</option>\n          <option value="500">500,0 mm²</option>'
content = content.replace(sec_html_old, sec_html_new)

# 5. Update metodoInstalacao HTML
met_html_old = r'<option value="d">D — Eletroduto enterrado</option>'
met_html_new = r'<option value="d">D — Eletroduto enterrado</option>\n          <option value="e">E — Cabo multipolar ao ar livre</option>\n          <option value="f">F — Cabos unipolares justapostos</option>\n          <option value="g">G — Cabos unipolares espaçados</option>'
content = content.replace(met_html_old, met_html_new)

# 6. Update onMaterialChange function
on_mat_old = r'''function onMaterialChange(){
  document.getElementById('alWarning').style.display=document.getElementById('materialCondutor').value==='al'?'block':'none';
  resetCalculado();
}'''
on_mat_new = r'''function onMaterialChange(){
  var mat=document.getElementById('materialCondutor').value;
  document.getElementById('alWarning').style.display=mat==='al'?'block':'none';
  var sel=document.getElementById('secaoSelecionada');
  for(var i=0;i<sel.options.length;i++){
    var val=parseFloat(sel.options[i].value);
    if(mat==='al'&&val<16){
      sel.options[i].disabled=true;
      sel.options[i].style.display='none';
    }else{
      sel.options[i].disabled=false;
      sel.options[i].style.display='';
    }
  }
  if(mat==='al'&&parseFloat(sel.value)<16) sel.value='16';
  resetCalculado();
}'''
content = content.replace(on_mat_old, on_mat_new)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched create_app.py successfully.")

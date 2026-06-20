# Script para Organizar Repositórios por Tópicos

Este script automatiza a adição de tópicos a todos os seus repositórios GitHub.

## Instalação

1. Clone este repositório ou baixe o arquivo `organize_repos.py`
2. Instale a dependência: `pip install requests`
3. Obtenha seu token em: https://github.com/settings/tokens

## Uso

```bash
python organize_repos.py seu_token_aqui
```

## Script Python

```python
#!/usr/bin/env python3
import requests
import sys

REPOS_CONFIG = {
    "aula01-python": ["python", "learning"],
    "Aula02listas_tuplas_dict_python": ["python", "learning"],
    "aula_git": ["python", "git"],
    "Aula_input_python": ["python", "learning"],
    "Aula_principais_metodos_string_python": ["python", "learning"],
    "Comparadores_operadores_python": ["python", "learning"],
    "estudos_codigos_python_casa": ["python", "learning"],
    "if_else_python": ["python", "learning"],
    "loop_python": ["python", "learning"],
    "while_python": ["python", "learning"],
    "while_True": ["python"],
    "teste_vscode": ["python"],
    "teste_home": ["python"],
    "streamlit_python": ["python", "streamlit"],
    "lista_tarefas_streamlit": ["python", "streamlit"],
    "sistema_biblioteca_streamlit": ["python", "streamlit"],
    "sistema_chamados_streamlit": ["python", "streamlit"],
    "projeto_tkinter": ["python", "tkinter"],
    "projeto_senha_tkinter": ["python", "tkinter"],
    "projeto_tkinter_hospital2": ["python", "tkinter"],
    "tkinter_projeto_hospital": ["python", "tkinter"],
    "front-end": ["html", "css", "web"],
    "portifolio-css": ["html", "css", "portfolio"],
    "projeto-tabela": ["html", "css", "web"],
    "site-loja": ["html", "css", "web"],
    "biblioteca_flet": ["python", "flet"],
    "inicio-aula-vscode": ["learning", "vscode"],
    "senai-git": ["learning", "course"],
    "skills-introduction-to-github": ["learning", "github"],
}

OWNER = "webcapcl"
API_BASE = "https://api.github.com"

def set_topics(token, repo_name, topics):
    url = f"{API_BASE}/repos/{OWNER}/{repo_name}/topics"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }
    data = {"names": topics}
    
    try:
        response = requests.put(url, json=data, headers=headers)
        response.raise_for_status()
        return True, "✅ OK"
    except Exception as e:
        return False, f"❌ Erro: {str(e)}"

def main():
    token = sys.argv[1]
    print("🚀 Iniciando organização dos repositórios...")
    success_count = 0
    
    for repo_name, topics in REPOS_CONFIG.items():
        print(f"📁 {repo_name}: {', '.join(topics)}")
        success, msg = set_topics(token, repo_name, topics)
        print(f"   {msg}")
        if success:
            success_count += 1
    
    print(f"\n✅ Completo! {success_count}/{len(REPOS_CONFIG)} repositórios atualizados")

if __name__ == "__main__":
    main()
```

## Para rodar:

1. Salve o código acima em um arquivo chamado `organize_repos.py`
2. Execute: `python organize_repos.py 60556536`
3. Pronto! Seus repositórios estarão organizados por tópicos

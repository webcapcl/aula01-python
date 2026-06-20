#!/usr/bin/env python3
"""
Script para organizar repositórios do GitHub por tópicos
Uso: python organize_repos.py <TOKEN_GITHUB>
"""

import requests
import sys

# Configuração dos repositórios e seus tópicos
REPOS_CONFIG = {
    # PYTHON
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
    
    # TKINTER
    "projeto_tkinter": ["python", "tkinter"],
    "projeto_senha_tkinter": ["python", "tkinter"],
    "projeto_tkinter_hospital2": ["python", "tkinter"],
    "tkinter_projeto_hospital": ["python", "tkinter"],
    
    # WEB/FRONTEND
    "front-end": ["html", "css", "web"],
    "portifolio-css": ["html", "css", "portfolio"],
    "projeto-tabela": ["html", "css", "web"],
    "site-loja": ["html", "css", "web"],
    
    # FLET
    "biblioteca_flet": ["python", "flet"],
    
    # OUTROS
    "inicio-aula-vscode": ["learning", "vscode"],
    "senai-git": ["learning", "course"],
    "skills-introduction-to-github": ["learning", "github"],
}

OWNER = "webcapcl"
API_BASE = "https://api.github.com"

def set_topics(token, repo_name, topics):
    """Adiciona tópicos a um repositório"""
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
    except requests.exceptions.HTTPError as e:
        return False, f"❌ Erro: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return False, f"❌ Erro: {str(e)}"

def main():
    if len(sys.argv) < 2:
        print("❌ Uso: python organize_repos.py <TOKEN_GITHUB>")
        print("Obtenha seu token em: https://github.com/settings/tokens")
        sys.exit(1)
    
    token = sys.argv[1]
    
    print("🚀 Iniciando organização dos repositórios...")
    print(f"📊 Total de repositórios: {len(REPOS_CONFIG)}\n")
    
    success_count = 0
    error_count = 0
    
    for repo_name, topics in REPOS_CONFIG.items():
        print(f"📁 {repo_name}")
        print(f"   Tópicos: {', '.join(topics)}")
        
        success, message = set_topics(token, repo_name, topics)
        print(f"   {message}")
        
        if success:
            success_count += 1
        else:
            error_count += 1
        print()
    
    print("=" * 60)
    print(f"✅ Sucesso: {success_count}")
    print(f"❌ Erros: {error_count}")
    print(f"📊 Total: {success_count + error_count}/{len(REPOS_CONFIG)}")
    print("=" * 60)
    
    if error_count == 0:
        print("\n🎉 Todos os repositórios foram organizados com sucesso!")
    else:
        print(f"\n⚠️ {error_count} repositório(s) falharam. Verifique o token.")

if __name__ == "__main__":
    main()

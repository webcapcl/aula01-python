#!/usr/bin/env python3
"""
Script para organizar repositórios do GitHub por tópicos
Execute: python run_organize.py
"""

import requests

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
TOKEN = "60556536"
API_BASE = "https://api.github.com"

def set_topics(repo_name, topics):
    """Adiciona tópicos a um repositório"""
    url = f"{API_BASE}/repos/{OWNER}/{repo_name}/topics"
    
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
    }
    
    data = {"names": topics}
    
    try:
        response = requests.put(url, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        return True, "✅ OK"
    except requests.exceptions.HTTPError as e:
        return False, f"❌ Erro: {e.response.status_code}"
    except Exception as e:
        return False, f"❌ Erro: {str(e)}"

def main():
    print("=" * 70)
    print("🚀 ORGANIZANDO REPOSITÓRIOS POR TÓPICOS".center(70))
    print("=" * 70)
    print(f"\n📊 Total de repositórios: {len(REPOS_CONFIG)}\n")
    
    success_count = 0
    error_count = 0
    errors = []
    
    for i, (repo_name, topics) in enumerate(REPOS_CONFIG.items(), 1):
        print(f"[{i:2d}/{len(REPOS_CONFIG)}] 📁 {repo_name}")
        print(f"        └─ Tópicos: {', '.join(topics)}", end=" → ")
        
        success, message = set_topics(repo_name, topics)
        print(message)
        
        if success:
            success_count += 1
        else:
            error_count += 1
            errors.append((repo_name, message))
    
    print("\n" + "=" * 70)
    print(f"✅ Sucesso: {success_count}/{len(REPOS_CONFIG)}")
    print(f"❌ Erros: {error_count}/{len(REPOS_CONFIG)}")
    print("=" * 70)
    
    if errors:
        print("\n⚠️ Repositórios com erro:")
        for repo, error in errors:
            print(f"  • {repo}: {error}")
    else:
        print("\n🎉 SUCESSO! Todos os repositórios foram organizados com tópicos!")
        print("\n📌 Você pode visualizar os tópicos em:")
        print("   https://github.com/webcapcl?tab=repositories")

if __name__ == "__main__":
    main()

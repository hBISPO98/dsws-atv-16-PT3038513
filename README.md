# Sistema de Gestão Acadêmica - Avaliação Semestral 📚

Aplicação web em **Flask**, com **Flask-Form**, desenvolvida para Avaliação Semestral. O projeto apresenta o menu completo de gestão acadêmica com foco funcional na rota de **Cadastro de Cursos**, mantendo uma arquitetura limpa e otimizada.

---

## 🚀 Estrutura e Funcionalidades

**1. Menu de Navegação Acadêmica**
- **Layout Completo:** A barra de navegação superior exibe todas as opções do sistema (como *Cadastro de Professores*, *Cadastro de Disciplinas*, *Cadastro de Alunos*, *Cadastro de Cursos* e *Cadastro de Ocorrências*).
- **Tratamento de Rotas Secundárias:** As secções fora do escopo principal redirecionam de forma limpa para páginas de conteúdo indisponível (nesta versão)

**2. Foco Funcional: aba de Cadastro de Cursos**
- **Modelo de Dados (`app/models.py`):** Estrutura dedicada exclusivamente à gestão de cursos (`id`, `nome`, `descricao`).
- **Validação de Formulários (`app/forms.py`):** Utilização do `CursoForm` com regras de validação para o nome e a descrição.
- **Ciclo de Listagem e Criação:** Vistas principais implementadas para o registo e visualização dinâmica dos cursos cadastrados (`cursos.html`, `index.html`, `base.html`).

---

## ⚙️ O que foi necessário implementar?

- **Integração com Flask-Form:** Configuração segura de formulários e tratamento de dados via POST.
- **Modularidade (Blueprints):** Organização do código da aplicação em torno do módulo principal (`app/main/`).
- **Gestão de Base de Dados:** Persistência otimizada com Flask-SQLAlchemy.

---

## 💡 Boas Práticas Adotadas

- **Interface Consistente:** Padronização visual através de templates base reutilizáveis.

---

## 👩🏽‍💻 Demonstração
<div align="center">

| Página Principal |
| :---: |
| <img src="https://github.com/user-attachments/assets/c1fde859-e832-4ba1-a9af-ad770bd05008" /> |

<br>

| Aba - Cadastro de Cursos |
| :---: |
| <img src="https://github.com/user-attachments/assets/0fb67e6f-e9ed-4af1-8183-1243e0aacc7b" /> |

<br>

| Outras Abas |
| :---: |
| <img src="https://github.com/user-attachments/assets/5cf698a8-e8ff-4e07-b8a8-d61cf2e762eb" /> |

</div>

> ⚠️ **Nota de Escopo (Versão Atual):**
> Informa-se que esta versão da aplicação foi redimensionada e otimizada exclusivamente para atender aos requisitos da avaliação final, concentrando-se unicamente na implementação do CRUD completo de **Cursos**. Outras rotas, (como gestão de professores ou módulos complementares presentes em versões anteriores) não desenvolvidas neste escopo, visando a entrega de uma aplicação enxuta.

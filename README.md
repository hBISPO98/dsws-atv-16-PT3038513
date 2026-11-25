# CRUD de Cursos - Aplicação da Avaliação Final 📚

Evolução de projeto web em Flask para a criação de uma aplicação lean focada exclusivamente num CRUD de **Cursos**. O objetivo desta versão foi realizar uma limpeza profunda de componentes legados (como autenticação, sistema de utilizadores e envio de e-mails), reestruturando a arquitetura para garantir um código otimizado, enxuto e pronto para publicação e avaliação.

---

## 🚀 O que mudou? (Versão Anterior vs. Versão Atual)

**1. Simplificação do Modelo de Dados (`app/models.py`)**
- **Foco exclusivo no CRUD:** Remoção completa dos modelos de utilizadores (`User`), papéis (`Role`) e autenticação, mantendo exclusivamente o modelo `Curso` (`id`, `nome`, `descricao`).

**2. Reestruturação dos Formulários e Vistas (`app/forms.py` e `app/main/views.py`)**
- **Consolidação de Formulários:** Centralização do formulário `CursoForm` na raiz da pasta `app/forms.py` com validações robustas de comprimento para o nome e a descrição.
- **Adaptação das Rotas:** Atualização das views principais para gerir o ciclo de vida completo de criação, listagem, edição e remoção de cursos.

**3. Limpeza de Interface e Templates (`app/templates/`)**
- **Remoção de Elementos Obsoletos:** Eliminação de templates de login, registo e e-mails (`auth/` e `mail/`), mantendo uma interface limpa e focada no template principal de cursos (`cursos.html`, `index.html`, `base.html`).

---

## ⚙️ O que foi necessário implementar?

- **Refatoração do Modelo `Curso`:** Definição limpa dos atributos do curso na base de dados utilizando o Flask-SQLAlchemy.
- **Centralização de Formulários (`app/forms.py`):** Configuração do `CursoForm` com campos validados por regras de comprimento e preenchimento obrigatório.
- **Limpeza de Estrutura e Resíduos:** Remoção de pacotes mortos (`app/auth/`, `app/email.py`, pasta `tests/` antiga e migrações de base de dados desatualizadas).

---

## 💡 Boas Práticas Adotadas

- **Arquitetura Enxuta (Lean):** Eliminação de código morto e dependências desnecessárias para garantir uma aplicação leve, segura e de fácil manutenção no PythonAnywhere.
- **Organização Modular:** Manutenção do padrão Flask Blueprints (`app/main/`) aliado a uma estrutura limpa e centralizada de formulários e modelos.

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

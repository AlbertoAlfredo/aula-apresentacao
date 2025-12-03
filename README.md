# 🏛️ Sistema Web de Cadastro de Patrimônio

## 📋 Contexto do Projeto

Este projeto foi desenvolvido como parte da **Etapa 2 (Avaliação Prática - "Aula Teste")** do Processo Seletivo SENAI para o cargo de **Instrutor de Formação Profissional III**, na Área de Tecnologia da Informação.

O objetivo principal é a criação de um sistema web funcional para gerenciar o cadastro de **Patrimônios** e **Setores**, conforme as especificações do edital.

---

## ✨ Funcionalidades Principais

O sistema implementa todas as operações CRUD (`Create`, `Read`, `Update`, `Delete`) para as duas entidades principais:

### 1. Gestão de Patrimônio
* **Cadastrar:** Adiciona novos ativos (nome, número de tombamento, etc.).
* **Visualizar:** Lista todos os patrimônios cadastrados.
* **Editar:** Permite a modificação dos dados de um patrimônio, incluindo a reatribuição a um novo setor.
* **Excluir:** Remove um patrimônio do sistema.

### 2. Gestão de Setores
* **Cadastrar:** Cria novos setores para organização dos ativos.
* **Visualizar:** Lista todos os setores.
* **Editar:** Permite a modificação do nome do setor.
* **Excluir (Restrita):** A exclusão de um setor é **impedida** caso haja algum patrimônio vinculado a ele (`ON DELETE RESTRICT` no SQLite). Isso garante a integridade referencial dos dados, conforme a lógica de negócio do projeto.

### 3. Relação e Arquitetura
* **Relacionamento:** Implementa a relação 1:N (Um Setor para Muitos Patrimônios) com chave estrangeira.
* **Responsividade:** O *design* da interface é responsivo para garantir a usabilidade em diversos dispositivos.

---

## 💻 Tecnologias e Arquitetura

O projeto segue um padrão de arquitetura simples e modular para facilitar o desenvolvimento e a manutenção, separando as responsabilidades em camadas.

| Componente | Tecnologia | Detalhes |
| :--- | :--- | :--- |
| **Backend/Core** | **Python** (Linguagem) & **Flask** (Micro-framework) | Responsável pela lógica de negócio, roteamento e comunicação com o banco de dados. |
| **Banco de Dados** | **SQLite3** | Banco de dados leve e embarcado. Acesso implementado com classes estáticas para CRUD. |
| **Frontend/UI** | **HTML5** & **Jinja2** | Renderização da interface. Utiliza **Macros Jinja2** para a reutilização de código (ex: ícones SVG) e limpeza do template. |
| **Estilização** | **Bootstrap** (CSS Framework) | Responsável pelo design e pela responsividade da interface. |
| **Comunicação** | **Custom Middleware** | Implementação de um middleware WSGI customizado para habilitar a submissão de métodos **PUT** e **DELETE** através de formulários HTML (enviados via POST com campo `_method` oculto). |

---

## 🚀 Como Configurar e Executar

Siga os passos abaixo para configurar e rodar a aplicação localmente.

### Pré-requisitos

* Python 3.x
* Pip (gerenciador de pacotes do Python)

### 1. Clone o Repositório

```bash
git clone [https://docs.github.com/pt/repositories/creating-and-managing-repositories/creating-a-new-repository](https://docs.github.com/pt/repositories/creating-and-managing-repositories/creating-a-new-repository)
cd aula-apresentacao
2. Instale as Dependências
O Flask e outras bibliotecas necessárias (listadas em requirements.txt) serão instaladas.

Bash

pip install -r requirements.txt
3. Inicialize o Banco de Dados
O banco de dados (banco.db) será criado automaticamente na primeira execução do bd.py (ou ao iniciar o main.py).

4. Execute a Aplicação
Inicie o servidor de desenvolvimento do Flask:

Bash

python main.py
5. Acesse o Sistema
O sistema estará acessível no seu navegador:

http://127.0.0.1:5000

📂 Estrutura do Projeto
A estrutura de arquivos segue a convenção do Flask e inclui módulos específicos para a arquitetura:

aula-apresentacao/
├── main.py             # Arquivo principal do Flask (Rotas e inicialização)
├── bd.py               # Módulo de Conexão e Lógica CRUD (Setor e Patrimônio)
├── banco.db            # Banco de dados SQLite
├── requirements.txt    # Dependências do projeto
├── templates/
│   ├── base.jinja      # Template base (header/footer/layout)
│   ├── setores.jinja   # Interface de listagem e exclusão de Setores
│   ├── ...             # Outros templates (formulários, patrimônios)
├── static/
│   ├── style.css       # Estilos customizados
│   └── bootstrap/      # Arquivos do Bootstrap
└── utils/
    └── middleware.py   # Implementação do HTTPMethodOverrideMiddleware
# 🤾‍♂️ Fit-App | Preparação Física - Handebol

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

> **🌐 Aplicação em Produção:** Acesse o app rodando ao vivo [clicando aqui](https://fitapp.pythonanywhere.com/).

Uma aplicação web responsiva (Mobile-First) desenvolvida para gerenciar, otimizar e rastrear as rotinas de preparação física de uma equipe universitária de handebol. 

O projeto substitui planilhas estáticas por uma interface interativa, permitindo que os atletas acompanhem seus treinos mensais, registrem cargas e marquem séries concluídas diretamente do celular durante o treino, com suporte a vídeos demonstrativos e funcionamento otimizado por cache local.

---

## ✨ Principais Funcionalidades

* **Roteamento Dinâmico de Treinos:** O back-end em Flask interpreta um "banco de dados" em memória (dicionários Python) para gerar rotas e submenus dinamicamente com base no mês e na categoria do treino (ex: Academia vs. Elástico/Peso Corporal).
* **Persistência de Dados (Local Storage):** Utilização avançada de `localStorage` via JavaScript para:
  * Salvar o progresso das séries (ex: 1/3, 2/3, Feito ✓).
  * Armazenar anotações textuais e cargas levantadas pelos atletas.
  * Lembrar a última planilha/mês selecionada pelo usuário, garantindo um redirecionamento inteligente no próximo acesso.
* **UI/UX Focada em Performance:** 
  * Design Mobile-First garantindo usabilidade com uma mão durante o treino.
  * *Dark Mode* integrado com detecção automática da preferência do sistema operacional e *toggle* manual.
  * Layout responsivo utilizando *CSS Flexbox* via Tailwind CSS para evitar quebra de interface em dispositivos com telas menores.
* **Separação de Ciclos de Treinamento:** Isolamento lógico entre treinos "Atemporais" (Mobilidade, Preventivos) e "Sazonais" (Planilhas mensais progressivas).

---

## 🛠️ Tecnologias Utilizadas

* **Back-end:** Python 3, Flask
* **Front-end:** HTML5, Tailwind CSS (via CDN para leveza), JavaScript Vanilla (DOM Manipulation & Web Storage API)
* **Controle de Versão:** Git, GitHub
* **Deploy/Hospedagem:** PythonAnywhere (WSGI configuration)

---

## 🏗️ Arquitetura do Projeto

O projeto adota uma arquitetura baseada em MVC (Model-View-Controller) simplificada para Flask:

```text
📁 Fit-App/
├── 📄 app.py              # Controller principal: Define o roteamento e a lógica de renderização.
├── 📄 treinos.py          # Model (Estático): Atua como banco de dados mapeando os meses e exercícios.
├── 📁 templates/          # Views: Arquivos HTML com Jinja2 templating.
│   ├── 📄 index.html      # Página inicial e seletor de ciclos de treino.
│   ├── 📄 submenu.html    # Interface intermediária para categorias com ramificações.
│   └── 📄 treino.html     # Ficha de execução do treino, lógica de progresso e inputs.
└── 📄 README.md

## 🚀 Como Executar Localmente (Para Desenvolvedores)

Se você é um desenvolvedor ou recrutador e deseja rodar a aplicação em ambiente local para testes ou contribuições, siga os passos abaixo:

Clone o repositório:

Bash
git clone [https://github.com/Eduzznet/Fit-App.git](https://github.com/Eduzznet/Fit-App.git)
cd Fit-App
Crie e ative um ambiente virtual (Opcional, mas recomendado):

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Instale as dependências:
O projeto requer apenas o Flask.

Bash
pip install Flask
Inicie o servidor local:

Bash
python app.py
Acesse no navegador:
Abra http://127.0.0.1:5000

🎯 Motivação e Aprendizado
Este projeto foi desenvolvido com o propósito de unir o estudo prático de Engenharia de Software com a rotina esportiva universitária. O desafio principal foi criar uma arquitetura que permitisse a adição mensal de novas planilhas de forma escalável (sem precisar criar novas páginas HTML), focando forte na Experiência do Usuário (UX) de atletas que precisam de um app rápido, simples e que lembre o seu progresso automaticamente sem a necessidade de criar sistemas complexos de login/senha em banco de dados para a equipe.
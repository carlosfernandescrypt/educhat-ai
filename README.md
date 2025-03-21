# EduChat - Assistente Educacional Inteligente

![EduChat Logo](https://via.placeholder.com/150x150.png?text=EduChat)

## 📚 Sobre o Projeto

EduChat é uma plataforma de assistência educacional que utiliza inteligência artificial para fornecer conteúdo personalizado para estudantes. O assistente adapta suas respostas de acordo com o nível educacional do usuário e sua área de interesse, proporcionando uma experiência de aprendizado mais eficaz e personalizada.

### 🌟 Principais Características

- **Adaptação ao Nível Educacional**: Personaliza o conteúdo para estudantes do Ensino Fundamental, Médio, Superior ou Pós-graduação
- **Áreas de Interesse**: Adapta explicações para diferentes áreas (Exatas, Humanas, Biológicas, Tecnologia, Linguagens)
- **Interface de Chat Intuitiva**: Interface de conversação amigável para facilitar a interação
- **Histórico de Conversas**: Armazena conversas anteriores para referência futura
- **Modo Offline**: Funciona mesmo quando a conexão com o serviço de IA não está disponível

## 🛠️ Tecnologias Utilizadas

### Back-end
- **Django**: Framework web
- **Django REST Framework**: API RESTful
- **SQLite**: Banco de dados
- **Ollama**: Integração com modelos de IA locais

### Front-end
- **React**: Biblioteca JavaScript para interfaces
- **React Router**: Navegação
- **Styled Components**: Estilização
- **Axios**: Requisições HTTP

## 📂 Estrutura do Projeto

O projeto está organizado em duas principais partes:

```
educhat/
├── back-end/                # Aplicação Django
│   ├── accounts/            # Módulo de autenticação e perfis de usuário
│   ├── chat/                # Módulo de chat e integração com IA
│   ├── educhat/             # Configurações do projeto Django
│   ├── db.sqlite3           # Banco de dados
│   └── manage.py            # Script de gerenciamento do Django
└── front-end/               # Aplicação React
    ├── eduai/               # Código fonte do front-end
    │   ├── public/          # Arquivos públicos
    │   └── src/             # Código fonte React
    │       ├── components/  # Componentes React
    │       ├── contexts/    # Contextos para gerenciamento de estado
    │       ├── services/    # Serviços e API
    │       └── styles/      # Arquivos de estilo
    ├── package.json         # Dependências do projeto
    └── package-lock.json    # Lock de dependências
```

## ⚙️ Requisitos

- Node.js (v14 ou superior)
- npm ou yarn
- Python (v3.8 ou superior)
- pip
- Ollama (opcional, para execução local dos modelos de IA)

## 🚀 Instalação e Execução

### Back-end (Django)

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/educhat.git
   cd educhat/back-end
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install django djangorestframework django-cors-headers python-dotenv requests
   ```

4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário (opcional):
   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

### Front-end (React)

1. Navegue até a pasta do front-end:
   ```bash
   cd educhat/front-end/eduai
   ```

2. Instale as dependências:
   ```bash
   npm install
   # ou
   yarn install
   ```

3. Inicie o servidor de desenvolvimento:
   ```bash
   npm start
   # ou
   yarn start
   ```

4. Acesse a aplicação em `http://localhost:3000`

### Configuração do Ollama (opcional)

Para utilizar o EduChat com o Ollama para processamento local:

1. Instale o Ollama seguindo as instruções em https://ollama.ai/
2. Execute o servidor Ollama:
   ```bash
   ollama serve
   ```
3. Baixe o modelo necessário:
   ```bash
   ollama pull llama2
   ```

## 💻 Uso

1. Crie uma conta ou faça login
2. Configure seu perfil educacional selecionando seu nível de educação e área de interesse
3. Inicie uma conversa com o assistente educacional
4. Faça perguntas relacionadas aos seus estudos e receba respostas personalizadas
5. Acesse seu histórico de conversas quando necessário

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Envie para a branch original (`git push origin feature/nova-feature`)
5. Crie um Pull Request

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## 📞 Contato

Para dúvidas ou sugestões, entre em contato através de [seu-email@exemplo.com].

---

Desenvolvido com ❤️ para apoiar a educação através da tecnologia.

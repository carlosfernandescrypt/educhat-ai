# EduChat - Documentação Técnica (Parte 1)

## 1. Visão Geral do Sistema

O EduChat é uma plataforma educacional interativa que utiliza inteligência artificial para fornecer assistência personalizada aos estudantes. O sistema adapta suas respostas com base no perfil educacional do usuário, criando uma experiência de aprendizado sob medida que considera tanto o nível educacional quanto a área de interesse do estudante.

### 1.1 Objetivos do Sistema

- Fornecer assistência educacional personalizada através de um chatbot inteligente
- Adaptar o conteúdo com base no nível de educação do usuário (Fundamental, Médio, Superior, Pós-graduação)
- Personalizar explicações de acordo com a área de interesse (Exatas, Humanas, Biológicas, Tecnologia, Linguagens)
- Manter histórico de conversas para referência futura
- Funcionar mesmo sem conexão com serviços de IA externos (modo offline)

### 1.2 Público-alvo

- Estudantes de todos os níveis educacionais (do Ensino Fundamental à Pós-graduação)
- Educadores que buscam ferramentas para auxiliar seus alunos
- Autodidatas que desejam um assistente de aprendizado personalizado

## 2. Arquitetura do Sistema

O EduChat implementa uma arquitetura cliente-servidor com separação clara entre front-end e back-end:

### 2.1 Componentes Principais

1. **Front-end (Cliente)**: 
   - Aplicação React que fornece a interface de usuário
   - Gerencia a autenticação e sessão de usuário no lado do cliente
   - Renderiza as conversas e histórico de mensagens
   - Comunica-se com o back-end via API REST

2. **Back-end (Servidor)**:
   - API Django REST Framework que gerencia lógica de negócios
   - Sistema de autenticação e gestão de usuários
   - Armazenamento e recuperação de conversas
   - Integração com serviço de IA (Ollama)

3. **Serviço de IA**:
   - Integração com o Ollama para processamento de linguagem natural
   - Modelo de fallback para funcionamento offline
   - Personalização de respostas com base no perfil do usuário

### 2.2 Diagrama de Arquitetura

```
┌─────────────┐      HTTP/JSON      ┌─────────────┐      API      ┌─────────────┐
│             │                     │             │               │             │
│  Front-end  │────────────────────▶│   Back-end  │──────────────▶│  Serviço IA │
│   (React)   │◀────────────────────│   (Django)  │◀──────────────│   (Ollama)  │
│             │                     │             │               │             │
└─────────────┘                     └─────────────┘               └─────────────┘
                                          │
                                          │
                                          ▼
                                    ┌─────────────┐
                                    │             │
                                    │  Banco de   │
                                    │    Dados    │
                                    │  (SQLite)   │
                                    │             │
                                    └─────────────┘
```

## 3. Módulos do Sistema

### 3.1 Módulo de Autenticação e Perfil de Usuário

Localizado no diretório `back-end/accounts/`, este módulo gerencia:

- Registro e autenticação de usuários
- Perfis educacionais personalizados (nível de educação e área de interesse)
- Atualização de informações de perfil

**Componentes principais:**
- `models.py`: Define o modelo `UserProfile` que estende o usuário padrão do Django
- `views.py`: Implementa as views para registro, login e gerenciamento de perfil
- `serializers.py`: Serializa dados de usuário para comunicação via API

### 3.2 Módulo de Chat

Localizado no diretório `back-end/chat/`, este módulo gerencia:

- Conversas e mensagens entre usuário e assistente
- Integração com o serviço de IA
- Personalização de respostas baseadas no perfil do usuário

**Componentes principais:**
- `models.py`: Define os modelos `Conversation` e `Message`
- `views.py`: Implementa endpoints para criar, listar e gerenciar conversas
- `ai_service.py`: Fornece integração com o Ollama e lógica de personalização de respostas

### 3.3 Interface de Usuário

Localizada no diretório `front-end/eduai/src/`, a interface é dividida em:

- **Componentes de Autenticação**: Gerenciam login e registro (`components/Auth/`)
- **Interface de Chat**: Renderiza conversas e processa mensagens (`components/Chat/`)
- **Contextos**: Gerenciam estado global da aplicação (`contexts/`)

## 4. Fluxo de Dados

### 4.1 Fluxo de Autenticação

1. Usuário acessa a aplicação e fornece credenciais (login) ou informações de registro
2. Front-end envia dados para o back-end através da API REST
3. Back-end valida as informações, cria sessão (se válido) e retorna token/dados de usuário
4. Front-end armazena as informações de autenticação e redireciona para a interface principal

### 4.2 Fluxo de Conversação

1. Usuário envia uma mensagem através da interface de chat
2. Front-end envia a mensagem para o back-end via API REST
3. Back-end armazena a mensagem no banco de dados
4. Back-end obtém o perfil do usuário (nível educacional e área de interesse)
5. Back-end envia a mensagem e dados de perfil para o serviço de IA
6. Serviço de IA processa a mensagem, personalizando a resposta com base no perfil
7. Back-end recebe a resposta, armazena no banco de dados e envia para o front-end
8. Front-end exibe a resposta na interface de chat

### 4.3 Fluxo de Gerenciamento de Conversas

1. Usuário acessa a lista de conversas anteriores
2. Front-end solicita os dados ao back-end
3. Back-end recupera as conversas do usuário do banco de dados
4. Front-end exibe a lista de conversas para seleção
5. Ao selecionar uma conversa, front-end solicita as mensagens relacionadas
6. Back-end recupera as mensagens da conversa específica
7. Front-end exibe o histórico completo da conversa selecionada

## 5. Modelo de Dados

### 5.1 Usuário e Perfil

```
User (Django built-in)
├── id: Integer (PK)
├── username: String
├── email: String
├── password: String
└── ...

UserProfile
├── id: Integer (PK)
├── user: ForeignKey(User)
├── nivel_educacao: Enum('fundamental', 'medio', 'superior', 'pos')
└── area_interesse: Enum('exatas', 'humanas', 'biologicas', 'tecnologia', 'linguagens', 'outros')
```

### 5.2 Conversa e Mensagens

```
Conversation
├── id: Integer (PK)
├── user: ForeignKey(User)
├── title: String
├── created_at: DateTime
└── updated_at: DateTime

Message
├── id: Integer (PK)
├── conversation: ForeignKey(Conversation)
├── role: Enum('user', 'assistant', 'system')
├── content: Text
└── created_at: DateTime
```

## 6. Personalização Educacional

A personalização das respostas é um diferencial do EduChat, realizada através dos seguintes mecanismos:

### 6.1 Adaptação ao Nível Educacional

O sistema adapta o conteúdo com base no nível educacional do usuário:

- **Ensino Fundamental**: Utiliza linguagem simples, explicações básicas e exemplos cotidianos
- **Ensino Médio**: Fornece explicações balanceadas com alguma profundidade técnica
- **Ensino Superior**: Emprega terminologia técnica apropriada e discussões mais profundas
- **Pós-graduação**: Utiliza terminologia especializada e aborda tópicos avançados

### 6.2 Adaptação à Área de Interesse

Além do nível educacional, o sistema personaliza as respostas considerando a área de interesse:

- **Ciências Exatas**: Enfatiza exemplos matemáticos, físicos ou químicos
- **Ciências Humanas**: Relaciona conceitos a contextos históricos, sociológicos ou filosóficos
- **Ciências Biológicas**: Enfoca exemplos biológicos, da saúde ou ambientais
- **Tecnologia**: Conecta conceitos a aplicações tecnológicas e desenvolvimento de software
- **Linguagens**: Relaciona conceitos a exemplos linguísticos, literatura ou comunicação

## 7. Segurança e Privacidade

### 7.1 Autenticação

- Utiliza o sistema de autenticação do Django para gerenciar usuários
- Implementa autenticação baseada em sessão com tokens
- Aplica validação de dados em formulários de registro e login

### 7.2 Autorização

- Controle de acesso baseado em usuário para conversas e mensagens
- Endpoints da API protegidos contra acesso não autorizado
- Usuários só têm acesso às suas próprias conversas e dados de perfil

### 7.3 Privacidade de Dados

- Armazenamento seguro de dados do usuário
- Processamento local de mensagens (quando usando Ollama)
- Sem compartilhamento de dados com serviços de terceiros (exceto quando configurado explicitamente)

## 8. Desafios Técnicos e Soluções

### 8.1 Funcionamento Offline

**Desafio**: Garantir que a aplicação funcione mesmo sem acesso ao serviço de IA.

**Solução**: Implementação de um serviço de fallback (`MockOllamaService`) que simula respostas básicas quando o Ollama não está disponível.

### 8.2 Personalização Contextual

**Desafio**: Adaptar respostas ao nível educacional e área de interesse do usuário.

**Solução**: Utilização de prompts de sistema personalizados que instruem o modelo de IA sobre como ajustar o tom, complexidade e exemplos com base no perfil do usuário.

### 8.3 Interface Responsiva

**Desafio**: Criar uma interface que funcione bem em diferentes dispositivos.

**Solução**: Implementação de design responsivo usando Styled Components com media queries para adaptar a interface a diferentes tamanhos de tela. 
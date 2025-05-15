# EduChat - Documentação Técnica (Parte 2)

## 1. Visão Geral

O EduChat é uma plataforma educacional que fornece assistência personalizada aos estudantes por meio de inteligência artificial. A solução permite que os usuários interajam com um assistente virtual que adapta suas respostas de acordo com o nível educacional e área de interesse específica de cada estudante, proporcionando uma experiência de aprendizado individualizada.

## 2. Tabela de Funcionalidades

| ID | Funcionalidade | Descrição | Prioridade |
|----|---------------|-----------|------------|
| F01 | Autenticação de Usuários | Sistema de cadastro e login para identificação de usuários | Alta |
| F02 | Perfil Educacional | Configuração do nível de educação e área de interesse | Alta |
| F03 | Chat Inteligente | Interface para troca de mensagens com o assistente de IA | Alta |
| F04 | Personalização de Respostas | Adaptação das respostas ao perfil do usuário | Alta |
| F05 | Histórico de Conversas | Armazenamento e visualização de conversas anteriores | Média |
| F06 | Edição de Perfil | Atualização de informações do perfil do usuário | Média |
| F07 | Criação de Novas Conversas | Capacidade de iniciar múltiplas conversas sobre temas diferentes | Média |
| F08 | Modo Offline | Funcionamento do sistema mesmo sem conexão com serviço de IA | Baixa |
| F09 | Interface Responsiva | Adaptação da interface para diferentes dispositivos | Média |

## 3. Levantamento e Análise de Requisitos

### 3.1 Entendimento do Problema

Estudantes de diferentes níveis educacionais enfrentam dificuldades ao buscar assistência personalizada para suas dúvidas acadêmicas. Os recursos educacionais tradicionais geralmente não conseguem adaptar-se adequadamente às necessidades específicas de cada aluno, considerando seu nível de conhecimento, área de interesse e estilo de aprendizagem.

Os principais problemas identificados são:
- Dificuldade em obter explicações adaptadas ao nível de conhecimento do estudante
- Falta de contextualização das respostas conforme a área de interesse
- Ausência de um assistente disponível a qualquer momento para esclarecer dúvidas
- Necessidade de manter histórico das conversas para referência futura

### 3.2 Requisitos Funcionais

| ID | Requisito | Descrição | Prioridade |
|----|-----------|-----------|------------|
| RF01 | Cadastro de usuário | Sistema deve permitir o cadastro de novos usuários com informações básicas | Alta |
| RF02 | Login | Sistema deve autenticar usuários cadastrados | Alta |
| RF03 | Configuração de perfil | Usuários devem poder definir nível educacional e área de interesse | Alta |
| RF04 | Envio de mensagens | Sistema deve permitir o envio de perguntas para o assistente | Alta |
| RF05 | Recebimento de respostas | Sistema deve fornecer respostas personalizadas do assistente | Alta |
| RF06 | Listagem de conversas | Sistema deve exibir lista de conversas anteriores do usuário | Média |
| RF07 | Visualização de histórico | Sistema deve permitir acessar o histórico completo de uma conversa | Média |
| RF08 | Criação de conversas | Sistema deve permitir iniciar novas conversas | Média |
| RF09 | Edição de título | Usuários devem poder editar o título das conversas | Baixa |
| RF10 | Exclusão de conversas | Sistema deve permitir excluir conversas | Baixa |

### 3.3 Requisitos Não Funcionais

| ID | Requisito | Descrição | Categoria |
|----|-----------|-----------|-----------|
| RNF01 | Responsividade | Interface deve se adaptar a diferentes tamanhos de tela | Usabilidade |
| RNF02 | Tempo de resposta | Sistema deve responder em até 3 segundos em condições normais | Performance |
| RNF03 | Disponibilidade | Sistema deve estar disponível mesmo sem conexão com serviço de IA externo | Disponibilidade |
| RNF04 | Segurança | Dados dos usuários devem ser armazenados de forma segura | Segurança |
| RNF05 | Escalabilidade | Sistema deve suportar crescimento no número de usuários | Escalabilidade |
| RNF06 | Personalização | Respostas devem ser adaptadas ao perfil educacional do usuário | Funcionalidade |
| RNF07 | Privacidade | Conversas e dados de usuários não devem ser compartilhados | Segurança |
| RNF08 | Compatibilidade | Sistema deve funcionar nos principais navegadores web | Compatibilidade |

## 4. Resumo de Usuários

| Nome | Responsabilidade | Descrição |
|------|------------------|-----------|
| Estudante Fundamental | Consumidor | Alunos do ensino fundamental que buscam auxílio em seus estudos, necessitando de explicações simples e exemplos cotidianos |
| Estudante Médio | Consumidor | Alunos do ensino médio que precisam de conteúdo equilibrado entre simplicidade e profundidade técnica |
| Estudante Superior | Consumidor | Estudantes universitários que buscam explicações com terminologia técnica apropriada e maior profundidade conceitual |
| Pós-graduando | Consumidor | Estudantes de pós-graduação que necessitam de discussões avançadas e conexões com pesquisas atuais |
| Professor | Facilitador | Educadores que utilizam a plataforma como ferramenta auxiliar para seus alunos |
| Administrador | Gerenciador | Responsável pela manutenção e configuração da plataforma |

## 5. Necessidades do Cliente

| ID | Necessidade | Prioridade | Solução Atual |
|----|-------------|------------|---------------|
| N01 | Obter assistência educacional personalizada | Alta | Tutores particulares, fóruns online, pesquisas gerais |
| N02 | Acesso a explicações adaptadas ao nível de conhecimento | Alta | Livros didáticos, vídeo-aulas genéricas |
| N03 | Contextualização das explicações conforme área de interesse | Média | Materiais específicos por disciplina, sem integração |
| N04 | Disponibilidade 24/7 para esclarecer dúvidas | Alta | Fóruns com tempo de resposta variável, consulta a materiais estáticos |
| N05 | Registro de conversas para revisão posterior | Média | Anotações manuais, salvamento de links |
| N06 | Interface intuitiva e de fácil uso | Alta | Aplicações educacionais com interfaces complexas |
| N07 | Funcionamento offline ou com conexão limitada | Baixa | Materiais físicos, downloads de conteúdo |

## 6. Representação Arquitetural

### 6.1 Visão Geral da Arquitetura

O EduChat implementa uma arquitetura cliente-servidor com três componentes principais:

1. **Cliente (Front-end)**: Aplicação React que fornece a interface de usuário e gerencia a interação com o usuário.
2. **Servidor (Back-end)**: API Django REST Framework que gerencia lógica de negócios, autenticação e armazenamento de dados.
3. **Serviço de IA**: Integração com Ollama para processamento de linguagem natural e geração de respostas personalizadas.

### 6.2 Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────────────┐
│                           Cliente                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │ Componentes │  │ Contextos   │  │ Serviços de Comunicação │  │
│  │ de Interface│  │ (Estado)    │  │ com API                 │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                          ▲
                          │ API REST
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                          Servidor                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │ Módulo de   │  │ Módulo de   │  │ Integração com Serviço  │  │
│  │ Usuários    │  │ Chat        │  │ de IA                   │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                          ▲
                          │ API Interna
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Serviço de IA (Ollama)                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │ Modelo de   │  │ Sistema de  │  │ Mecanismo de            │  │
│  │ Linguagem   │  │ Prompts     │  │ Fallback                │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## 7. Metas e Restrições da Arquitetura

### 7.1 Metas Arquiteturais

- **Modularidade**: Permitir que os componentes sejam desenvolvidos, testados e mantidos independentemente
- **Extensibilidade**: Facilitar a adição de novas funcionalidades e integração com outros serviços
- **Manutenibilidade**: Código estruturado para facilitar correções e atualizações
- **Responsividade**: Interface adaptável a diferentes dispositivos e tamanhos de tela
- **Desempenho**: Garantir tempos de resposta aceitáveis mesmo com crescimento de usuários
- **Disponibilidade**: Funcionamento contínuo mesmo com indisponibilidade temporária de serviços externos

### 7.2 Restrições Arquiteturais

- **Tecnológicas**:
  - Front-end: React, React Router, Styled Components
  - Back-end: Django, Django REST Framework
  - Banco de Dados: SQLite (desenvolvimento), PostgreSQL (produção)
  - Integração IA: Ollama (local) ou serviços compatíveis

- **Ambiente**:
  - Hospedagem em servidores web padrão com suporte a Python
  - Necessidade de configuração de servidor para execução do Ollama (opcional)
  - Acesso a API de serviço de IA alternativo caso não utilize Ollama

- **Segurança**:
  - Autenticação obrigatória para acesso às funcionalidades
  - Proteção contra acesso não autorizado a dados de outros usuários
  - Armazenamento seguro de credenciais e dados sensíveis

- **Desempenho**:
  - Tempo máximo de resposta da interface de 1 segundo
  - Tempo máximo de geração de resposta da IA de 5 segundos
  - Suporte a múltiplos usuários simultâneos
``` 
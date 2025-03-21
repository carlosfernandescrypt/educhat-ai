# backend/chat/ai_service.py

import requests
import json
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class OllamaService:
    def __init__(self):
        self.api_url = settings.OLLAMA_API_URL
        self.model = settings.OLLAMA_MODEL
        
    def get_educational_system_prompt(self, nivel_educacao=None, area_interesse=None):
        """Cria um prompt de sistema educacional personalizado com base no perfil do usuário"""
        
        # Prompt base
        prompt = """Você é um assistente educacional especializado que ajuda estudantes a aprender. 
Seu objetivo é fornecer explicações claras, precisas e adaptadas ao nível do estudante.
Use exemplos práticos sempre que possível para ilustrar conceitos.
Se não souber a resposta, admita honestamente em vez de inventar informações.
Incentive o pensamento crítico e a resolução de problemas.
"""

        # Adaptar ao nível educacional
        if nivel_educacao:
            if nivel_educacao == 'fundamental':
                prompt += """
O usuário está no Ensino Fundamental. Use linguagem simples, explicações básicas e exemplos do cotidiano.
Evite termos técnicos e conceitos complexos sem explicação adequada.
"""
            elif nivel_educacao == 'medio':
                prompt += """
O usuário está no Ensino Médio. Use explicações balanceadas com alguma profundidade técnica.
Relacione os conceitos com aplicações práticas e explique os fundamentos principais.
"""
            elif nivel_educacao == 'superior':
                prompt += """
O usuário está no Ensino Superior. Você pode usar terminologia técnica apropriada e discussões mais profundas.
Relacione os conceitos com suas aplicações no campo profissional e pesquisa atual.
"""
            elif nivel_educacao == 'pos':
                prompt += """
O usuário está na Pós-graduação. Você pode usar terminologia especializada e discutir tópicos avançados.
Relacione os conceitos com pesquisas recentes e discussões acadêmicas no campo.
"""

        # Adaptar à área de interesse
        if area_interesse:
            prompt += f"\nO usuário tem interesse particular em {area_interesse.capitalize()}. "
            
            if area_interesse == 'exatas':
                prompt += "Apresente exemplos matemáticos, físicos ou químicos quando apropriado."
            elif area_interesse == 'humanas':
                prompt += "Relacione conceitos a contextos históricos, sociológicos ou filosóficos quando relevante."
            elif area_interesse == 'biologicas':
                prompt += "Relacione conceitos a exemplos biológicos, da saúde ou ambientais quando apropriado."
            elif area_interesse == 'tecnologia':
                prompt += "Conecte conceitos a aplicações tecnológicas e desenvolvimento de software quando relevante."
            elif area_interesse == 'linguagens':
                prompt += "Relacione conceitos a exemplos linguísticos, literatura ou comunicação quando relevante."
            
        return prompt
        
    def generate_response(self, messages, nivel_educacao=None, area_interesse=None):
        """
        Gera uma resposta a partir do modelo Ollama com base no histórico de mensagens
        """
        try:
            # Preparar mensagens no formato que o Ollama espera
            formatted_messages = []
            
            # Adicionar prompt de sistema educacional
            system_prompt = self.get_educational_system_prompt(nivel_educacao, area_interesse)
            formatted_messages.append({"role": "system", "content": system_prompt})
            
            # Adicionar mensagens da conversa
            for message in messages:
                formatted_messages.append({
                    "role": message.role,
                    "content": message.content
                })
            
            # Preparar payload para a API do Ollama
            payload = {
                "model": self.model,
                "messages": formatted_messages,
                "stream": False
            }
            
            # Fazer a requisição para o Ollama
            response = requests.post(self.api_url, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                return result.get("message", {}).get("content", "Desculpe, não consegui gerar uma resposta.")
            else:
                logger.error(f"Erro na API Ollama: {response.status_code} - {response.text}")
                return "Desculpe, ocorreu um erro ao processar sua solicitação. Tente novamente mais tarde."
                
        except Exception as e:
            logger.error(f"Erro ao gerar resposta: {str(e)}")
            return "Desculpe, ocorreu um erro ao processar sua solicitação. Tente novamente mais tarde."

# Implementação de fallback para desenvolvimento sem Ollama rodando localmente
class MockOllamaService:
    def __init__(self):
        pass
        
    def get_educational_system_prompt(self, nivel_educacao=None, area_interesse=None):
        # Mesmo método da classe real para manter compatibilidade
        return "Você é um assistente educacional de demonstração."
        
    def generate_response(self, messages, nivel_educacao=None, area_interesse=None):
        """
        Simula uma resposta para desenvolvimento quando Ollama não está disponível
        """
        # Verificar se há mensagens
        if not messages:
            return "Olá! Como posso ajudar você hoje com seus estudos?"
        
        # Obter a última mensagem
        last_message = messages[-1]
        
        # Resposta simulada baseada no conteúdo da última mensagem
        if "matemática" in last_message.content.lower():
            return "A matemática é fundamental para o desenvolvimento do raciocínio lógico. Como posso ajudar você com esse assunto?"
        elif "história" in last_message.content.lower():
            return "A história nos ajuda a compreender o mundo atual através dos acontecimentos do passado. Qual período ou tema específico você está estudando?"
        elif "ciências" in last_message.content.lower():
            return "As ciências nos ajudam a entender como o mundo natural funciona. Você está interessado em biologia, química, física ou outra área específica?"
        elif "literatura" in last_message.content.lower():
            return "A literatura nos permite explorar diferentes mundos e experiências através das palavras. Você está lendo algum livro específico ou estudando algum autor ou período literário?"
        elif "computação" in last_message.content.lower() or "programação" in last_message.content.lower():
            return "A programação é uma habilidade fundamental no mundo digital. Você está aprendendo alguma linguagem específica ou tem algum projeto em mente?"
        else:
            return "Esse é um tema interessante para estudarmos! Poderia me dar mais detalhes sobre o que você gostaria de aprender ou qual dúvida você tem?"

# Função para escolher qual serviço usar (real ou mock)
def get_ai_service():
    try:
        # Tenta fazer uma requisição simples para ver se o Ollama está disponível
        requests.get(settings.OLLAMA_API_URL.replace('/api/generate', '/api/tags'))
        return OllamaService()
    except:
        # Se não conseguir conectar, usa o serviço simulado
        return MockOllamaService()
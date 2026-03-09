import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool
from langchain_anthropic import ChatAnthropic # Import do Claude

load_dotenv()

# Configura o "Cérebro" (Claude 3.5 Sonnet é o mais brabo pra isso)
claude_llm = ChatAnthropic(
    model='claude-3-5-sonnet-20240620',
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 1. Ferramenta
file_tool = FileReadTool()

# 2. Agente (Passamos o 'llm' aqui)
analista_sre = Agent(
    role='Especialista em Performance Linux',
    goal='Analisar logs de sistema e sugerir correções de kernel.',
    backstory='Você é um veterano com 20 anos de kernel Linux, mestre em resolver OOM e Kernel Panic.',
    tools=[file_tool],
    llm=claude_llm, # <--- O Agente agora usa o Claude
    verbose=True
)

# 3. Tarefa
tarefa_analise = Task(
    description='Leia o arquivo "logs_servidor.txt" e identifique o erro.',
    expected_output='Um resumo técnico do erro e o comando Linux para resolver.',
    agent=analista_sre
)

# 4. A Crew
minha_crew = Crew(
    agents=[analista_sre],
    tasks=[tarefa_analise]
)

print("### Iniciando com Anthropic Claude ###")
resultado = minha_crew.kickoff()
print(resultado)

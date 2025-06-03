import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

from utils.sql_tool import run_sql
from utils.prompt import get_prompt

load_dotenv()

llm = ChatOpenAI(model="gpt-4", temperature=0)

# Загрузка схемы
with open("schema_description.txt", encoding="utf-8") as f:
    schema = f.read()

# Инструмент выполнения SQL
def sql_agent_tool(query: str):
    return run_sql(query)

sql_tool = Tool(
    name="SQL DB",
    func=sql_agent_tool,
    description="Инструмент для выполнения SQL-запросов к базе данных"
)

# Создание агента
agent = initialize_agent(
    tools=[sql_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Основной цикл
if __name__ == "__main__":
    user_question = input("Введите вопрос: ")
    prompt = get_prompt().format(schema=schema, question=user_question)
    sql_query = llm.predict(prompt)

    print("\n[Сгенерированный SQL]:")
    print(sql_query)

    headers, results = run_sql(sql_query)
    print("\n[Результаты запроса]:")
    print(headers)
    for row in results:
        print(row)

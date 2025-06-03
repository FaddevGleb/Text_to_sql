from langchain.prompts import PromptTemplate

TEMPLATE = """
Ты SQL-ассистент. Используй только доступную схему базы данных ниже для создания SQL:

{schema}

Вопрос пользователя: {question}

Ответь ТОЛЬКО SQL-запросом, без пояснений.
"""

def get_prompt():
    return PromptTemplate(
        input_variables=["schema", "question"],
        template=TEMPLATE
    )

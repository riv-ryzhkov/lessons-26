
import key # ключ спрятан в отдельном файле
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent  # новый импорт без warning
import os


# Используем OpenRouter с бесплатной моделью Llama 3.1
llm = ChatOpenAI(
    model="meta-llama/llama-3.1-8b-instruct:free",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key= key.key  # вставьте ваш ключ
)

# ВАЖНО: вставьте сюда свой настоящий API-ключ OpenAI
# Он должен начинаться с "sk-" и содержать ТОЛЬКО латинские буквы, цифры и дефисы
# os.environ["OPENAI_API_KEY"] = key.key


# 1. Создаём ИНСТРУМЕНТЫ
@tool
def get_weather(city: str) -> str:
    """Узнает текущую погоду в указанном городе. Используй, если спрашивают о погоде."""
    weather_data = {
        "Москва": "+22°C, солнечно",
        "Лондон": "+15°C, дождь",
        "Дубай": "+38°C, ясно"
    }
    return weather_data.get(city, f"Не удалось найти погоду для города {city}")


@tool
def get_user_balance(user_id: int) -> str:
    """Проверяет финансовый баланс пользователя по его ID. Используй, если спрашивают про деньги или баланс."""
    return f"Баланс пользователя с ID {user_id} составляет 15 400 рублей."


# 2. Инициализируем LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# 3. Создаём агента
tools = [get_weather, get_user_balance]
agent = create_agent(llm, tools)


# 4. Функция для удобного запуска
def run_agent(query: str):
    """Запускает агента с заданным вопросом"""
    result = agent.invoke({"messages": [("user", query)]})
    return result["messages"][-1].content


# 5. Тестируем
if __name__ == "__main__":
    print("--- Тест 1: Запрос погоды ---")
    print(run_agent("Какая сейчас погода в Москве?"))

    print("\n--- Тест 2: Запрос баланса ---")
    print(run_agent("Сколько денег на счету у пользователя с ID 42?"))

    print("\n--- Тест 3: Комплексный запрос ---")
    print(run_agent("Проверь баланс пользователя 105 и скажи, какая погода в Дубае"))
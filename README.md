# Career AI Agent

Telegram-бот, который помогает отвечать на вопросы ИИ-рекрутеров на карьерных сайтах.

## Возможности

- выбор резюме;
- загрузка вакансии по URL;
- парсинг HH.ru;
- кэширование вакансии и резюме в Redis;
- ответы через OpenRouter;
- автоматические повторные запросы при ошибках 429.

## Структура

```
Telegram
      │
      ▼
Handlers
      │
      ▼
Services
      │
 ┌────┼─────┐
 ▼    ▼     ▼
LLM Cache Parser
```

## Запуск

```bash
cp .env.example .env
```

Заполнить:

- TELEGRAM_TOKEN
- OPENROUTER_API_KEY

Запуск:

```bash
cd docker

docker compose up --build
```

## Тесты

```bash
pytest
```

## Использование

```
/start

↓

URL вакансии

↓

Резюме

↓

Вопрос

↓

Ответ LLM
```
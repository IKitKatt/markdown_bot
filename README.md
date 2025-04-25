## Что это такое

Простой бот в **Telegram** для конвертации **Markdown** разметки в разметку **Telegram**

### Принцип действия

1. Активируем бота через ```/start```
2. Отправляем текст в **Markdown** разметке
3. Получаем на выходе тот же текст, но в разметке **Telegram**


## Развертывание

1. Клонируем репозиторий
2. Редактируем ``TELEGRAM_TOKEN`` на свое значение
```dockerfile
version: '3.8'

services:
  telegram-bot:
    container_name: markdown_bot
    build: .
    environment:
      - TELEGRAM_TOKEN=${TELEGRAM_TOKEN}
    restart: unless-stopped   
```
3. Собираем **docker-compose** через ``docker-compose up -d``
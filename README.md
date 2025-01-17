# Car broke prediction

## Описание проекта
Данный проект пор дисциплинам ML и Python предназначен для предсказания вида поломки автомобиля и расстояния до поломки автомобиля для успешного построения оптимального плана обслуживания.

---

## Используемые технологии
- **Python 3.12**: язык программирования
- **FastAPI**: для создания API
- **PostgreSQL**: для хранения данных
- **Scikit-learn / CatBoost / Optuna**: для машинного обучения
- **Docker**: для контейнеризации приложения
- **Git**: для управления версиями
- **Poetry**: для сборки и управлления зависимостями
---

## Инструкции по запуску

### Шаг 1. Клонируйте репозиторий
```bash
git clone https://github.com/vivichv9/mai-ml-project
cd mai-ml-project
```

### Шаг 2. Запуск docker контейнера
```bash
docker compose build && docker compose up -d
```
После выполненных действий запустится сервер в контейнере и сервис будет доступен на порту 8000.
Доступ к предсказанию будет доступен через HTTP запрос

```bash
curl http://localhost:8000/ml/predict/
```

## Инструкция по обучению модели

### Шаг 1. Создайте виртуальное окружение poetry

```bash
poetry shell
```

### Шаг 2. Установите зависимости

```bash
poetry install
```

### Шаг 3. Запустите скрипт обучения модели в виртуальном окружении poetry

```bash
python -m ml.service.model_train
```

## Примечание
#### Для работы с проектом необходим доступ к базе данных, а именно ее URL в файле .env с именем переменной DATBASE_URL
```bash
DATABASE_URL=<CONNECTION_URL>
```

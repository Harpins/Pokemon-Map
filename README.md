# Пример сайта, посвященного игре типа "ловля монстров", взаимодействующего с базой данных (БД) SQLite. 

На главной странице отображается карта города Москва, с указанием местоположения всех существ, присутствующих в БД на определённый промежуток времени. В верхней части сайта отображаются карточки видов, присутствующих в БД. На карте может быть несколько индивидуальных особей одного и того же вида: например, 2 Бульбазавра. 

![2024-11-17_19-26-18](https://github.com/user-attachments/assets/91f4a4c1-c59f-479b-9133-d789920a6e6b)

При переходе по ссылке на карточке вида открывается страница описания существ данного вида, включая стихийный тип и варианты развития (при наличии). Ниже расположена карта Москвы с координатами существ данного вида.
![2024-11-17_19-29-46](https://github.com/user-attachments/assets/f7ed9476-a87e-4a8c-93f1-f0d5d2f85f36)

В БД можно помещать виды существ, элементы существ и индивидуальные особи. 

- Параметры вида существ:
  1. ID вида 
  2. Название вида на трех языках (ру., англ., яп.)
  3. Описание вида 
  4. Ссылка на изображение, используемое для отображения местоположения на карте и для создания карточки вида.
  5. Предыдущая и следующая стадии развития (при наличии) существа данного вида
  6. Элемент(ы) из соответствующей модели
     
- Параметры индивидуальной особи:
  1. Идентификатор UUID, генерируемый автоматически
  2. Вид существа (из соответствующей модели)
  3. Координаты местоположения (широта и долгота),
  4. Даты появления и исчезновения (`.datetime`) особи
  5. Боевые характеристики особи (уровень, здоровье, атака, защита, спец., скорость)
     
- Параметры элемента:
  1. Название элемента
  2. Ссылка на изображение элемента
  3. Текстовое описание элемента

### Как запустить

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Затем установите зависимости

```sh
pip install -r requirements.txt
```

Проведите миграцию данных в БД:

```sh
python manage.py makemigrations
python manage.py migrate
```

Настройте учетную запись админа:

```sh
python manage.py createsuperuser
```
Далее по инструкции ввести логин, e-mail и пароль

Запустите разработческий сервер

```sh
python manage.py runserver
```

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

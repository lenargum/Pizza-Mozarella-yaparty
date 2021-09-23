# Yandex party - Хакатон: Лаборатория Медиасервисов

### Команда - Pizza Mozzarella

```Галеев Фарит, Гумеров Ленар, Крашенинников Игорь, Соловьев Роман, Юрин Артем```

# Сопутствующие материалы

1. Репозиторий с сервисом общих плейлистов - https://github.com/HiGal/PartyRecommender
2. Figma - https://www.figma.com/team_invite/redeem/Gy2y1R6gmhrxkiOMiGesFL - Дизайн и mindmap
3. Google Drive - https://drive.google.com/drive/folders/11Miz4fMGyvA1UOk2z2u6LejdFGDIluI4?sort=13&direction=a -
   интервью, roadmap, презентация
4. Сам сервис - http://yaparty.ml

# Y.Party games

## Run locally

```
cd games_backend/app
python3 main.py
```

## Run in docker

### Image

```
cd games_backend
docker build -t games_backend .
```

### Container

```
docker run --name games_backend_main -p 8000:8000 games_backend
```

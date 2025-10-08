from labyrinth_game.schemas.room import Rooms, RoomSchema, Directions
from enum import Enum

class Commamds(Enum):
    solve = "solve"

# список всех комнат:
ROOMS: dict[Rooms, RoomSchema] = {
    Rooms.entrance: RoomSchema(
        description='Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый факел.',
        exits={
            Directions.north: Rooms.hall,
            Directions.east: Rooms.trap_room
        },
        items=['torch'],
        puzzle=None
    ),
    Rooms.hall: RoomSchema(
        description='Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        exits={
            Directions.south: Rooms.entrance,
            Directions.west: Rooms.library,
            Directions.north: Rooms.treasure_room,
            Directions.down: Rooms.basement
        },
        items=[],
        puzzle=(
            'На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.',
            '10'
        )
    ),
    Rooms.trap_room: RoomSchema(
        description='Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
        exits={Directions.west: Rooms.entrance},
        items=['rusty_key'],
        puzzle=(
            'Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")',
            'шаг шаг шаг'
        )
    ),
    Rooms.library: RoomSchema(
        description='Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
        exits={
            Directions.east: Rooms.hall,
            Directions.north: Rooms.armory
        },
        items=['ancient_book'],
        puzzle=(
            'В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)',
            'резонанс'
        )
    ),
    Rooms.armory: RoomSchema(
        description='Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
        exits={Directions.south: Rooms.library},
        items=['sword', 'bronze_box'],
        puzzle=None
    ),
    Rooms.treasure_room: RoomSchema(
        description='Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
        exits={Directions.south: Rooms.hall},
        items=['treasure_chest'],
        puzzle=(
            'Дверь защищена кодом. Введите код (подсказка: это число пятикратного шага, 2*5= ? )',
            '10'
        )
    ),
    Rooms.mirror_room: RoomSchema(
        description='Стены этой комнаты покрыты зеркалами. В центре — странный портал.',
        exits={
            Directions.east: Rooms.treasure_room,
            Directions.west: Rooms.illusion_corridor
        },
        items=['broken_mirror_piece'],
        puzzle=(
            'Портал открывается только если вы скажете слово "свет" задом наперёд (введите его)',
            'тес'
        )
    ),
    Rooms.illusion_corridor: RoomSchema(
        description='Узкий коридор с иллюзией дверей. Кажется, здесь что-то спрятано.',
        exits={Directions.east: Rooms.mirror_room},
        items=['illusion_key'],
        puzzle=(
            'На стене надпись: "Я не существую, но меня можно увидеть. Что я?" (ответ одно слово)',
            'тень'
        )
    ),
    Rooms.basement: RoomSchema(
        description='Холодный подвал с сырым каменным полом. В углу стоит старый грубый стол, на котором видны следы крови.',
        exits={
            Directions.up: Rooms.hall,
            Directions.north: Rooms.torture_chamber
        },
        items=['old_chain', 'bloodied_key'],
        puzzle=(
            'На стене надпись: "Я всегда рядом, но меня не увидишь. Что я?" (ответ одно слово)',
            'звук'
        )
    ),
    Rooms.torture_chamber: RoomSchema(  # Исправлено с "torture_chamber"
        description='Пугающая пыточная комната. Здесь много железных инструментов, цепей и столов для допросов. Воздух тяжелый и мрачный.',
        exits={Directions.south: Rooms.basement},
        items=['iron_hook', 'broken_shackles'],
        puzzle=(
            'На стене вырезан вопрос: "Что может говорить без голоса, путешествовать без ног и быть видимым в зеркале?"',
            'отражение'
        )
    )
}

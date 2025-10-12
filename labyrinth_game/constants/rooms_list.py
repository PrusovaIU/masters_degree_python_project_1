from labyrinth_game.constants.direction import Directions
from labyrinth_game.constants.item import Items
from labyrinth_game.constants.room import Rooms
from labyrinth_game.schemas.puzzle import Puzzle
from labyrinth_game.schemas.room import RoomSchema

ROOMS: dict[Rooms, RoomSchema] = {
    Rooms.entrance: RoomSchema(
        description='Вы в темном входе лабиринта. Стены покрыты мхом. '
                    'На полу лежит старый факел.',
        exits={
            Directions.north: Rooms.hall,
            Directions.east: Rooms.trap_room
        },
        items=[Items.torch],
        puzzle=None,
        trap=False
    ),
    Rooms.hall: RoomSchema(
        description='Большой зал с эхом. По центру стоит пьедестал с '
                    'запечатанным сундуком.',
        exits={
            Directions.south: Rooms.entrance,
            Directions.west: Rooms.library,
            Directions.north: Rooms.treasure_room
        },
        items=[],
        puzzle=Puzzle(
            text='На пьедестале надпись: "Назовите число, которое идет после '
                 'девяти". Введите ответ цифрой.',
            answer='10',
            prize=Items.gold_coin
        ),
        trap=False
    ),
    Rooms.trap_room: RoomSchema(
        description='Комната с хитрой плиточной поломкой. На стене видна '
                    'надпись: "Осторожно — ловушка".',
        exits={
            Directions.west: Rooms.entrance,
            Directions.down: Rooms.basement
        },
        items=[Items.rusty_key],
        puzzle=Puzzle(
            text='Система плит активна. Чтобы пройти, назовите слово "шаг" '
                'три раза подряд (введите "шаг шаг шаг")',
            answer='шаг шаг шаг',
            prize=None
        ),
        trap=True
    ),
    Rooms.library: RoomSchema(
        description='Пыльная библиотека. На полках старые свитки. '
                    'Где-то здесь может быть ключ от сокровищницы.',
        exits={
            Directions.east: Rooms.hall,
            Directions.north: Rooms.armory
        },
        items=[Items.ancient_book],
        puzzle=Puzzle(
            text='В одном свитке загадка: "Что растет, когда его съедают?" '
                 '(ответ одно слово)',
            answer='резонанс',
            prize=Items.gold_coin
        ),
        trap=True
    ),
    Rooms.armory: RoomSchema(
        description='Старая оружейная комната. На стене висит меч, '
                    'рядом — небольшая бронзовая шкатулка.',
        exits={Directions.south: Rooms.library},
        items=[Items.sword, Items.bronze_box],
        puzzle=None,
        trap=False
    ),
    Rooms.treasure_room: RoomSchema(
        description='Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
        exits={Directions.south: Rooms.hall},
        items=[Items.treasure_chest],
        puzzle=Puzzle(
            text='Дверь защищена кодом. Введите код '
            '(подсказка: это число пятикратного шага, 2*5= ? )',
            answer='10',
            prize=Items.gold_coin
        ),
        trap=True
    ),
    Rooms.mirror_room: RoomSchema(
        description='Стены этой комнаты покрыты зеркалами. '
                    'В центре — странный портал.',
        exits={
            Directions.east: Rooms.treasure_room,
            Directions.west: Rooms.illusion_corridor
        },
        items=[Items.broken_mirror_piece],
        puzzle=Puzzle(
            text='Портал открывается только если вы скажете слово "свет" задом '
                 'наперёд (введите его)',
            answer='тевс',
            prize=Items.gold_coin
        ),
        trap=False
    ),
    Rooms.illusion_corridor: RoomSchema(
        description='Узкий коридор с иллюзией дверей. Кажется, здесь что-то спрятано.',
        exits={Directions.east: Rooms.mirror_room},
        items=[Items.illusion_key],
        puzzle=Puzzle(
            text='На стене надпись: "Я не существую, но меня можно увидеть. '
                 'Что я?" (ответ одно слово)',
            answer='тень',
            prize=None
        ),
        trap=False
    ),
    Rooms.basement: RoomSchema(
        description='Холодный подвал с сырым каменным полом. В углу стоит старый грубый стол, на котором видны следы крови.',
        exits={
            Directions.up: Rooms.trap_room,
            Directions.north: Rooms.torture_chamber
        },
        items=[Items.old_chain, Items.bloodied_key],
        puzzle=Puzzle(
            text='На стене надпись: "Я всегда рядом, но меня не увидишь. '
                 'Что я?" (ответ одно слово)',
            answer='звук',
            prize=None
        ),
        trap=True
    ),
    Rooms.torture_chamber: RoomSchema(  # Исправлено с "torture_chamber"
        description='Пугающая пыточная комната. Здесь много железных инструментов, цепей и столов для допросов. Воздух тяжелый и мрачный.',
        exits={Directions.south: Rooms.basement},
        items=[Items.iron_hook, Items.broken_shackles, Items.treasure_key],
        puzzle=Puzzle(
            text='На стене вырезан вопрос: "Что может говорить без голоса, '
                 'путешествовать без ног и быть видимым в зеркале?"',
            answer='отражение',
            prize=Items.gold_coin
        ),
        trap=True
    )
}

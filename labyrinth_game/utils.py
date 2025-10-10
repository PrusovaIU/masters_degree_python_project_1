def user_input(promt: str, allowed_answer: list[str]) -> str:
    """
    Функция для получения ввода пользователя.

    :param promt: текст для вывода в консоль.
    :param allowed_answer: список допустимых ответов.
    :return: введенный пользователем ответ.
    """
    info = f"{promt} ({'/'.join(allowed_answer)}): "
    while True:
        command = input(info).strip().lower()
        if command not in allowed_answer:
            print("Неверная команда!")
        else:
            return command

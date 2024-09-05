import re


def add_name_prefixes(text: str, name_len: int = 1):

    """
    Функция для добавления к каждому предложению префикса - имени автора предложения.
    Параметры:
        text - текст встречи в формате строки
        name_len - длина имён участников встречи
    Возвращает:
        строку из предложений вида: "Имя: предложение."
    """

    # Массив из предложений с добавленными именами
    prefixed_text = []

    # Делим исходный текст на предложения по разделителям, учитывая возможность дробных чисел и сокращений.
    sentences = re.split(r'(?<=[.!?])(?<!\d\.\d)(?<![a-z]\.\s)(?!\d)', text)

    # В конце после разделителя может быть добавлена пустая строка или строка сосотящая из пробелов и переноса строки. Удалим ее:
    if sentences[-1].strip() == "" or sentences[-1].strip() == "\n":
        sentences.pop()

    # Текущее имя, которое добавляется в начало предложений, не имеющих имени в начале.
    current_prefix = ""

    # Обрабатываем каждое предложение
    for sentence in sentences:
        # Находим индекс двоеточия в предложении
        sep_ind = sentence.find(":")

        # Если двоеточие есть, значит возможно перед двоеточием есть имя автора предложения
        if sep_ind != -1:
            # Считаем количество слов до двоеточия
            prefix_word_count = len(sentence[0:sep_ind+1].split())

            # Количество слов в имени может быть только равным name_len, поэтому
            # если слов получилось больше, значит это не имя
            if prefix_word_count > name_len:
                prefixed_text.append(current_prefix + " " + sentence)

            # Иначе это новое имя
            else:
                current_prefix = sentence[0:sep_ind+1]
                prefixed_text.append(sentence)

        # Если двоеточия в предложении нет, значит добавляем в его начало имя автора предыдущего предложения
        else:
            prefixed_text.append(current_prefix + " " + sentence)

    # Возвращаем строку
    return " ".join(prefixed_text)

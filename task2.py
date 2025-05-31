def alphabet(file_n):
    # В файле помимо длины в первой строке есть еще какое-то число, его игнорим
    # А еще у вас пример неправильный - там должно быть выведено 26 :)))))
    with open(file_n, "r") as f:
        n, _= (map(int, f.readline().strip().split()))
        sequence = list(map(int, f.readline().strip().split()))
  
    # Проверка наличия всех 26 чисел
    if len(set(sequence)) < 26:
        print("NONE")
        return

    # Инициализация
    count = [0] * 27  # Массив для подсчёта вхождений чисел (индекс 0 не используется)
    distinct = 0  # Количество уникальных чисел в окне
    min_length = float('inf')  # Минимальная длина окна
    left = 0  # Левый указатель

    # Скользящее окно
    for right in range(n):
        # Добавляем элемент в окно
        count[sequence[right]] += 1
        if count[sequence[right]] == 1:  # Если число встретилось впервые
            distinct += 1

        # Пытаемся сократить окно, если найдены все 26 чисел
        while distinct == 26:
            min_length = min(min_length, right - left + 1)
            # Удаляем элемент с левого конца
            count[sequence[left]] -= 1
            if count[sequence[left]] == 0:  # Если число больше не встречается
                distinct -= 1
            left += 1

    # Вывод результата
    if min_length == float('inf'):
        print("NONE")
    else:
        print(min_length)

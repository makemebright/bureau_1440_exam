def segments_intersection(file_n):
    with open(file_n, "r") as f:
        n = int(f.readline().strip())  # Количество отрезков
        segments = []
        for _ in range(n):
            l, r = map(int, f.readline().strip().split())  # Начало и конец отрезка
            segments.append((l, r))

    # Сделаем спискок всех концов оттезка (левых и правых) с пометками:
    ends = []
    for i in range(n):
        ends.append((segments[i][0], 0, i))  # Левый конец: (координата, 0, номер отрезка)
        ends.append((segments[i][1], 1, i))  # Правый конец: (координата, 1, номер отрезка)

    # Сортируем концы: по координате и при равенстве левые концы идут первыми
    ends.sort()

    # Инициализируем стек для активных отрезков и массив для покрытых отрезков
    stack = []
    covered = [False] * n
    points = []  # Список выбранных точек

    # Обрабатываем отсортированные концы
    for coord, type_, seg_num in ends:
        if type_ == 0:  # Левый конец
            stack.append(seg_num)  # Добавляем отрезок в стек
        else:  # Правый конец
            if not covered[seg_num]:  # Если отрезок не покрыт
                points.append(coord)  # Добавляем точку
                # Отмечаем все отрезки в стеке как покрытые
                while stack:
                    covered[stack.pop()] = True

    # Резульат - длина списка выбранных точек
    print(len(points))  # Количество точек

segments_intersection("data_prog_contest_problem_1.txt")

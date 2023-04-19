
array = [int(x) for x in input("Введите числа от 1 до 999 в любом порядке, через пробел: ").split()]

def merge_sort(array):  # функция мердж сорт для сортировки слиянием
    if len(array) < 2:  # если длинна масива меньше 2
        return array[:]  # вернуть массив
    else:
        middle = len(array) // 2 # середина = длинна масива //
        left = merge_sort(array[:middle])  # лево = сортировка слиянием (массив[срез до середины от начала
        right = merge_sort(array[middle:]) # право = сортировка слиянием (массив[срез до середины от начала
        return merge(left, right)  # выполняем слияние лефт и райт


def merge(left, right):# выполняем слияние лефт и райт
    result = [] # запишем результат
    i, j = 0, 0 # выставляем значение переменным

    while i < len(left) and j < len(right): # пока ай меньше длинны лефт и джей меньше длинны райт
        if left[i] < right[j]: # если лефт ай меньше райт джей
            result.append(left[i]) # добавим в результат лефт ай
            i += 1
        else:
            result.append(right[j]) #добавим в результат райт джей
            j += 1

    while i < len(left):         # пока ай меньше длинны лефт результат добавляем лефт ай
        result.append(left[i])
        i += 1

    while j < len(right):         # пока джей меньше длинны райт результат добавляем райт джей
        result.append(right[j])
        j += 1

    return result        # вернем результат

print(merge_sort(array)) # принт сортировка слиянием (массив ))


def binary_search(array, element, left, right): # назначем функцию бинарный поиск
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


while True:
    try:
        element = int(input("Введите число от 1 до 999 из введенных ранее : "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неправильный диапазон!")


print(binary_search(array, element, 0,  len(array)))
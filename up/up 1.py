all_tickets = int(input('Введите количество билетов: '))

numbers_ages = [] #возвраст участника(ов)
# для каждого билета запросить возраст
# Заполняем numbers_ages числами, которые вводит пользователь
for i in range(0, all_tickets):
    input_value = int(input(f'Введите возраст участника №{i + 1}:\n'))
    numbers_ages.append(input_value)
#соотнести цена / возвраст
def prise(age):
 for i in range (0, all_tickets):
    if age <18:
        return 0
    elif 18<= age <25:
        return 990
    else:
        return 1390
#общая стоимость тикетов
tickets_prise=sum(map(prise, numbers_ages))
#расчёт скидки в случае намба тикет > 3
discount_prise=int(tickets_prise*0.9)
if all_tickets >3:
    print('Стоимость всех билетов со скидкой: ', discount_prise, "руб.")
else:
    print('Стоимость всех билетов: ', tickets_prise, "руб.")

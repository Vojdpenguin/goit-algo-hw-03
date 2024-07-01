import random


def get_numbers_ticket(min, max, quantity):
    lst = []
    if min < 1 or max > 1000:
        return lst
    for num in range(min, max + 1):
        lst.append(num)
    numbers_ticket = random.sample(lst, k=quantity)
    numbers_ticket.sort()
    return numbers_ticket


print(f"Ваші лотерейні білети:{get_numbers_ticket(1, 10000, 10)}")
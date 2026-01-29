def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    _count_days(days, 1)


def _count_days(days: int, current_day: int):
    if current_day > days:
        print("Harvest time!")
        return
    else:
        print(f"Day {current_day}")
        _count_days(days, current_day + 1)

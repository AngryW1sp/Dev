import datetime
import pickle

DATE_FORMAT = "%d.%m.%Y"
with open("dict.txt", "rb+") as f:
    goods = pickle.load(f)


def add(items: dict) -> None:
    """Функция добовляет продукт в холодильник"""

    title = input("""Введите название продукта: """).strip()
    amount = input("Введите кол-во добовляемого продукта: ")
    date = datetime.datetime.strptime(
        input(
            "Введите срок годности продукта в формате\
            DD.MM.YYYY: "
        ),
        DATE_FORMAT,
    ).date()
    if title not in items:
        items[title] = [{"Кол-во:": amount, "Годен до:": date}]
    else:
        items[title].append({"Кол-во:": amount, "Годен до:": date})


def choice():
    print(
        """
    ------------------------------------------
    Выберите нужную функцию :
      1. Добавить продукт в холодильник
      2. Информация о продуктах в холодильнике
      3. Забрать продукт из холодильника
      4. Найти продукт в холодильнике
    ------------------------------------------
   """
    )
    input_choise = input("Введите номер операции: ")
    if input_choise == "1":
        add(goods)


def expire(items, in_advance_days=7):

    count = 1
    print("    В ближайшую неделю просрочятся:")
    print()

    for item in items:
        for food in items[item]:
            if food["Годен до:"] != "-":
                delta = food["Годен до:"] - datetime.datetime.now().date()
                if delta.days <= in_advance_days and delta.days > 0:
                    amount = food["Кол-во:"]
                    food_expire = food["Годен до:"].strftime(DATE_FORMAT)
                    print(
                        f"    {count}. {item} в кол-ве {amount}, Дата \
                            окончания срока годности: {food_expire}"
                    )
                    count += 1
    count = 1
    print()
    print()
    print("    Пора выбрасывать:")
    print()
    for item in items:
        for food in items[item]:
            if food["Годен до:"] != "-":
                delta = food["Годен до:"] - datetime.datetime.now().date()
                if delta.days < 0:
                    amount = food["Кол-во:"]
                    food_expire = food["Годен до:"].strftime(DATE_FORMAT)
                    print(
                        f"{count}. {item} в кол-ве {amount}, Дата окончания \
                            срока годности: {food_expire} "
                    )
                    count += 1


print('Здравствуйте! Вас приветствует приложение "Холодильник v 2.0"!')
print(
    f"""

    ---------------------------------------

    На данный момент в холодильнике находится {len(goods)} видов продуктов.

      """
)

expire(goods)
choice()


with open("dict.txt", "rb+") as f:
    pickle.dump(goods, f)

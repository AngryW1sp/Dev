import datetime
import pickle


DATE_FORMAT = "%d.%m.%Y"
with open("dict.txt", "rb+") as f:
    goods = pickle.load(f)


def add(items):
    title = input("""Введите название продукта: """).strip()
    amount = input("Введите кол-во добовляемого продукта: ")
    date = datetime.datetime.strptime(
        input("Введите срок годности продукта в формате DD.MM.YYYY: "), DATE_FORMAT
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
        for object in items[item]:
            if object["Годен до:"] != "-":
                delta = object["Годен до:"] - datetime.datetime.now().date()
                if delta.days <= in_advance_days and delta.days > 0:
                    amount = object["Кол-во:"]
                    object_expire = object["Годен до:"].strftime(DATE_FORMAT)
                    print(
                        f"    {count}. {item} в кол-ве {amount}, Дата окончания срока годности: {object_expire} "
                    )
                    count += 1
    count = 1
    print()
    print()
    print("    Пора выбрасывать:")
    print()
    for item in items:
        for object in items[item]:
            if object["Годен до:"] != "-":
                delta = object["Годен до:"] - datetime.datetime.now().date()
                if delta.days < 0:
                    amount = object["Кол-во:"]
                    object_expire = object["Годен до:"].strftime(DATE_FORMAT)
                    print(
                        f"    {count}. {item} в кол-ве {amount}, Дата окончания срока годности: {object_expire} "
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

'''SOLID. 5 складових цього принципу'''
'''Принцип єдиної відповідальності (Single responsibility)
З SRP добре пов'язаний прийом – виділення класу. Це коли з великого класу з безліччю слабо-пов'язаних за змістом полів та методів, виділяється один або кілька класів. Суть у тому, щоб явно виділити призначення класу або, іншими словами, виділити клас, який можна описати однією фразою.'''
# from math import pi
# class Person:
#     def __init__(self, name, zip, city, street):
#         self.name = name
#         self.zip = zip
#         self.city = city
#         self.street = street

#     def get_address(self):
#         return f'{self.zip}, {self.city}, {self.street}'

# person = Person('Alexander', '36007', 'Poltava', 'European, 28')
# print(person.get_address())

'''У нас є клас Person. Відповідно до принципу єдиної відповідальності клас повинен вирішувати лише якесь одне завдання. Зараз він вирішує два: зберігає дані користувача та виконує логіку перетворення адреси користувача.
Необхідно зробити так, щоб клас Person працював тільки з даними користувача, а завдання перетворення адреси делегувалося іншому екземпляру класу PersonAddress через залежність у конструкторі.'''
# class PersonAddress:
#     def __init__(self, zip, city, street):
#         self.zip = zip
#         self.city = city
#         self.street = street

#     def value_of(self):
#         return f'{self.zip}, {self.city}, {self.street}'

# class Person:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

#     def get_address(self):
#         return self.address.value_of()

# if __name__ == '__main__':
#     person = Person('Alexander', PersonAddress(
#         '36007', 'Poltava', 'European, 28'))
#     print(person.get_address())
    
'''Тепер ми дотримуємося принципу єдиної відповідальності.'''
#############################
'''Принцип відкритості-закритості (Open-closed)
Цей принцип допомагає вирішувати проблему, коли невелика зміна в одній частині системи викликає лавину змін в інших частинах. Якщо у програмі при зміні поліпшення потрібно виправити десятки модулів, така система, швидше за все, спроектована погано.Принцип відкритості-закритості декларує, що модулі повинні бути відкриті для розширення, але закриті для зміни.
Іншими словами — модулі потрібно проектувати так, щоб їх не можна було змінювати, а нова функціональність у програмі повинна з'являтися лише за допомогою створення нових сутностей та композиції їх зі старими.'''
# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

# def total_area(shapes):
#     sum = 0
#     for el in shapes:
#         sum += el.width * el.height
#     return sum

# if __name__ == '__main__':
#     shapes = [Rect(10, 10), Rect(4, 5), Rect(3, 3)]
#     area = total_area(shapes)
#     print(area)

'''Є клас Rect, що описує прямокутник, і є функція total_area, яка обчислює загальну площу фігур. У чому може виникнути неприємність для такого коду?
Якщо у нас з'явиться нова фігура, наприклад, коло — Circle, нам доведеться змінити роботу функції total_area.'''
# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

# def total_area(shapes):
#     sum = 0
#     for el in shapes:
#         if isinstance(el, Rect):
#             sum += el.width * el.height
#         if isinstance(el, Circle):
#             sum += el.radius ** 2 * pi
#     return sum

# if __name__ == '__main__':
#     shapes = [Rect(10, 10), Circle(5), Rect(4, 5), Rect(3, 3), Circle(3)]
#     area = total_area(shapes)
#     print(area)
'''І з появою нової фігури нам потрібно щоразу вносити зміни в роботу функції total_area. Щоб виправити ситуацію, потрібно перекласти обчислення площі фігури на самі класи:'''
# from math import pi

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area_of(self):
#         return self.width * self.height

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area_of(self):
#         return self.radius ** 2 * pi

# def total_area(shapes):
#     sum = 0
#     for el in shapes:
#         sum += el.area_of()
#     return sum

# if __name__ == '__main__':
#     shapes = [Rect(10, 10), Circle(5), Rect(4, 5), Rect(3, 3), Circle(3)]
#     area = total_area(shapes)
#     print(area)
'''Тепер все добре, і при появі нової фігури вносити зміну в роботу функції total_area більше не потрібно.'''
###########################
'''Принцип підстановки Барбари Лісков (Liskov substitution)
Принцип відкритості-закритості говорить про те, що у добре спроектованих програмах нова функціональність вводиться шляхом додавання нового коду, а не зміною старого, що вже працює. Принцип підстановки Лісков (далі LSP) — це як реалізувати цей принцип при побудові ієрархії наслідування класів в об'єктно-орієнтованих мовах програмування. По суті, правильна ієрархія наслідування в ООП - це ієрархія, побудована відповідно до LSP, щоб відповідати принципу відкритості-закритості.

У попередньому прикладі порушенням LSP була функція:'''
# def total_area(shapes):
#     sum = 0
#     for el in shapes:
#         if isinstance(el, Rect):
#             sum += el.width * el.height
#         if isinstance(el, Circle):
#             sum += el.radius ** 2 * pi
#     return sum
'''Тепер давайте розглянемо, як можна порушити LSP не таким очевидним способом. Припустимо, ми розробляємо програму, яка працює з геометричними фігурами. У ній є клас для роботи з прямокутниками:'''
# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def set_width(self, width):
#         self.width = width

#     def set_height(self, height):
#         self.height = height

#     def area_of(self):
#         return self.width * self.height
'''Тепер потрібно реалізувати фігуру квадрат. Квадрат – це очевидно прямокутник і цілком логічно, що клас Square повинен бути спадкоємцем класу Rect.'''
# class Square(Rect):
#     def __init__(self, size):
#         Rect.__init__(self, size, size)

#     def set_width(self, width):
#         self.width = width
#         self.height = width

#     def set_height(self, height):
#         self.width = height
#         self.height = height
'''І якщо у функції ми використовуємо клас Rect, а працюємо з конкретним класом Square, то можуть виникнути проблеми:'''
# def test_shape_size(shape):
#     shape.set_width(10)
#     shape.set_height(20)
#     return shape.area_of() == 200  # умова не спрацює, якщо shape — екземпляр класу Square
'''Відповідно до LSP нам необхідно використовувати спільний інтерфейс для обох класів і не наслідувати Square від Rect. Цей спільний інтерфейс повинен бути таким, щоб класи-спадкоємці могли б використовуватися замість батьківських класів, від яких вони утворені, не порушуючи роботу програми.'''
# from enum import Enum

# class SideType(Enum):
#     TYPE_WIDTH = 'width'
#     TYPE_HEIGHT = 'height'

# class Shape:
#     def set_side(self, size, side):
#         pass

#     def area_of(self):
#         pass

# class Rect(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def set_side(self, size, side):
#         if SideType.TYPE_WIDTH == side:
#             self.width = size
#         if SideType.TYPE_HEIGHT == side:
#             self.height = size

#     def set_width(self, width):
#         self.set_side(width, SideType.TYPE_WIDTH)

#     def set_height(self, height):
#         self.set_side(height, SideType.TYPE_HEIGHT)

#     def area_of(self):
#         return self.width * self.height

# class Square(Shape):
#     def __init__(self, size):
#         self.edge = size

#     def set_side(self, size, side=None):
#         self.edge = size

#     def set_width(self, width):
#         self.set_side(width)

#     def area_of(self):
#         return self.edge ** 2

# def get_area_of_shape(figure: Shape):
#     return figure.area_of()
    
# if __name__ == '__main__':
#     square = Square(10)
#     rect = Rect(5, 10)
#     print('Square area: ', get_area_of_shape(square))
#     print('Rect area: ', get_area_of_shape(rect))

'''Тепер поведінка спадкоємців не конфліктує із поведінкою базового класу. Це дозволить використовувати і Rect, і Square там, де оголошено використання Shape.'''
###########################
'''Принцип розділення інтерфейсу (Interface segregation)
Сутності не повинні залежати від інтерфейсів, які вони не використовують.
Коли принцип порушується, модулі схильні до всіх змін в інтерфейсах, від яких вони залежать. Це призводить до високої зв'язаності модулів один з одним.
ISP допомагає проектувати інтерфейси так, щоб зміни зачіпали тільки ті модулі, на функціональність яких вони справді впливають. Найчастіше це змушує інтерфейси дробити (розділяти).
Припустимо, що у нас є клас Programmer, який описує програміста з офісу деякої компанії. Співробітники пишуть код та іноді їдять піцу, яку компанія замовляє в офіс.'''
# class Programmer:
#     def write_code(self):
#         pass

#     def eat_pizza(self, slice_count):
#         pass

# class OfficeProgrammer(Programmer):
#     def __init__(self, name):
#         self.name = name

#     def eat_pizza(self, slice_count):
#         print(f'{self.name} eat {slice_count} slice pizza!')

#     def write_code(self):
#         print(f'{self.name} write code!')
'''Через деякий час компанія почала наймати фрілансерів, які працюють віддалено і піцу не їдять. Якщо ми використовуємо той самий інтерфейс, то клас RemoteProgrammer повинен буде реалізувати метод eat_pizza, хоча він йому і не потрібен.'''
# class RemoteProgrammer(Programmer):
#     def __init__(self, name):
#         self.name = name

#     def write_code(self):
#         print(f'{self.name} write code!')

#     def eat_pizza(self, slice_count):
#         pass
'''Ми можемо уникнути проблеми з прикладу вище, якщо розділимо клас Programmer. Ми можемо поділити його на дві ролі: CodeProducer та PizzaConsumer.'''
# class CodeProducer:
#     def write_code(self):
#         pass

# class PizzaConsumer:
#     def eat_pizza(self, slice_count):
#         pass

# class OfficeProgrammer(CodeProducer, PizzaConsumer):
#     def __init__(self, name):
#         self.name = name

#     def eat_pizza(self, slice_count):
#         print(f'{self.name} eat {slice_count} slice pizza!')

#     def write_code(self):
#         print(f'{self.name} write code!')

# class RemoteProgrammer(CodeProducer):
#     def __init__(self, name):
#         self.name = name

#     def write_code(self):
#         print(f'{self.name} write code!')
'''Тепер і OfficeProgrammer, і RemoteProgrammer будуть реалізовувати лише ті інтерфейси, які їм справді потрібні.'''
##########################
'''Принцип інверсії залежностей (Dependency inversion)
Відповідно до принципу, класи повинні залежати від інших класів не напряму, а від абстракцій. Класи верхніх рівнів не повинні залежати від класів нижніх рівнів. Обидва типи класів повинні залежати від абстракцій. Абстракції не повинні залежати від деталей. Деталі повинні залежати від абстракцій. У процесі розробки програмного забезпечення існує момент, коли функціонал застосунку перестає поміщатися в межах одного модуля або класу. Коли це відбувається, нам доводиться вирішувати проблему залежностей класів (модулів). В результаті, наприклад, може виявитися так, що високорівневі компоненти залежать від низькорівневих компонентів.'''
# import requests

# class RequestConnection:
#     def __init__(self, request):
#         self.request = request

#     def get_json_from_url(self, url):
#         return self.request.get(url).json()

# class ApiClient:
#     def __init__(self, fetch: RequestConnection):
#         self.fetch = fetch

#     def get_data(self, url):
#         response = self.fetch.get_json_from_url(url)
#         return response

# def data_adapter(data: dict):
#     return [{f"{el.get('ccy')}": {"buy": float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]

# def pretty_view(data):
#     pattern = '|{:^10}|{:^10}|{:^10}|'
#     print(pattern.format('currency', 'sale', 'buy'))
#     for el in data:
#         currency, *_ = el.keys()
#         buy = el.get(currency).get('buy')
#         sale = el.get(currency).get('sale')
#         print(pattern.format(currency, sale, buy))

# if __name__ == '__main__':
#     api_client = ApiClient(RequestConnection(requests))
    
#     data = api_client.get_data('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
#     pretty_view(data_adapter(data))
'''Клас ApiClient (високорівневий модуль) залежить від класу RequestConnection (абстракція). Він не використовує пакет requests напряму. Надалі це, наприклад, дозволить підмінити пакет requests всередині класу RequestConnection, не зачіпаючи роботу класу ApiClient. У прикладі ми знаходимо курс продажу долара та євро на поточну дату за допомогою API ПриватБанк.'''

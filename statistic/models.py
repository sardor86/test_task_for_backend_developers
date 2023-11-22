from django.db.models import Model, CharField, DateField, PositiveIntegerField, ForeignKey, RESTRICT, CASCADE


class Client(Model):
    fullname = CharField(
        'Полное имя клиента',
        max_length=120)
    birthdate = DateField('День рождение клиента')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Employee(Model):
    fullname = CharField(
        'Полное имя клиента',
        max_length=120
    )
    birthdate = DateField('День рождение сотрудника')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Product(Model):
    name = CharField(
        'Название продукта',
        max_length=50
    )
    quantity = PositiveIntegerField()
    price = PositiveIntegerField()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(Model):
    client = ForeignKey(Client, on_delete=RESTRICT)
    product = ForeignKey(Product, on_delete=RESTRICT)
    employee = ForeignKey(Employee, on_delete=CASCADE)
    date = DateField('Время заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

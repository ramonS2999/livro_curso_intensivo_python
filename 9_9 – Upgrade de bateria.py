print('''
            9.9 – Upgrade de bateria: Use a última versão de electric_car.py desta seção.
            Acrescente um método chamado upgrade_battery() na classe Battery. Esse
            método deve verificar a capacidade da bateria e defini-la com 85 se o valor
            for diferente. Crie um carro elétrico com uma capacidade de bateria default,
            chame get_range() uma vez e, em seguida, chame get_range() uma segunda
            vez após fazer um upgrade da bateria. Você deverá ver um aumento na
            distância que o carro é capaz de percorrer.
''')

from electric_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


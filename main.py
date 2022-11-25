london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vel": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
""" Задание 1.1. """
device = input('Введите имя устройства: ')
print(london_co[device])
"""Задание 1.2. """
#parameter = input('Введите имя параметра: ')
#print(london_co[device][parameter])
"""Заданиме 1.3. """
parameter = (','.join(london_co[device].keys()))
#parameters = input('Введите имя параметра (' + parameters + '): ')
#parameter = input('Введите имя параметра({parameters}):'.format(parameters=parameters))
parameter = input(f'Введите имя параметра({parameter}):')
parameter = parameter.lower()
print(london_co[device].get(parameter, 'Такого параметра нет'))


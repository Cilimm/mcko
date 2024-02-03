f = open('space.txt')
a = []
for i in f:
    a.append(i)
a.pop(0)

input_string = ''
while input_string != 'stop':
    input_string = input()
    ShipName_string = ''
    planet_string = ''
    direction_string = ''
    check = False
    for i in range(len(a)):
        ShipName, planet, coord_place, direction = map(str, a[0].split())
        if input_string == ShipName:
            check = True
            ShipName_string = ShipName
            planet_string = planet
            direction_string = direction
            break
    if check:
        print('Корабль ' + ShipName_string + ' был отправлен с планеты: ' + planet_string + ' и его направление движения было ' + direction_string)
    else:
        print('error.. er.. ror..')

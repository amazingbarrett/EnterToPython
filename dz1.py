duration=int(input())
while duration<59:
    print(duration,'секунд')
    break
while 3600>duration>59:
    s=duration%60
    m=duration//60
    print(m, 'минут', s, 'секунд')
    break
while 86400>duration>3600:
    s=duration%60
    m=duration//60
    h=m//60
    m=m-(h*60)
    print(h,'часов', m, 'минут', s,'секунд')
    break
while duration>86400:
    s=duration%60
    m=duration//60
    h=m//60
    d=h//24
    m=m-(h*60)
    h=h-(d*24)
    print(d, 'дней',h ,'часов', m, 'минут', s, 'секунд')
    break




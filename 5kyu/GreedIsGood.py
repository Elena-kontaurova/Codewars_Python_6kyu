'''Greed - это игра в кости, в которую играют пятью шестигранными кубиками. 
Ваша миссия, если вы решите принять ее, состоит в том, чтобы забросить мяч в соответствии с этими правилами. 
Вам всегда будет предоставлен массив с пятью значениями шестигранных кубиков.'''
def score(dice):
    result = 0
    for d in range(1,7):
        k = dice.count(d)
        if k >= 3:
            result += 1000 if d == 1 else d *100
            k -= 3
        result  += 100*k if d == 1 else 50 * k if d == 5 else 0
    return result
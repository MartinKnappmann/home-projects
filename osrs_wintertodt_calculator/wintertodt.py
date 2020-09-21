# https://oldschool.runescape.wiki/w/Wintertodt
# this calculator is used for calculating wintertodts attack
# Attack type	Formula
# Standard attack	(16-W-2*B)*(HP+1)/FM
# Brazier attack	(10-W)*(HP+1)/FM
# Area attack	    (10-W)*(HP+1)/FM
# FM = Base Firemaking level
# HP = Base Hitpoints level
# W = Number of warm items worn, where the maximum value is 4
# B = Number of braziers lit, where the maximum value is 3


def calculate(HP, FM, W, B):

    std_atk = (16 - W - 2 * B) * (HP + 1) / FM
    brz_atk = ((10 - W) * (HP + 1) / FM) * 2
    are_atk = brz_atk * (3 / 2)

    return std_atk, brz_atk, are_atk


def manual_calculate():

    HP = int(input('Enter hitpoint level: '))
    FM = int(input('Enter Firemaking level: '))
    W = int(input('Enter number of warm items worn: '))
    B = int(input('Enter number of braziers lit: '))

    s, b, a = calculate(HP, FM, W, B)

    print('#######################\n'
          '# Standard attack: {} #\n'
          '# Brazier attack:  {} #\n'
          '# Area attack:     {} #\n'
          '#######################'.format(s, b, a))


def auto_calculate(): 

    import matplotlib.pyplot as plt

    W = 2
    B = 3
    FM = 99
    samples = list(range(10, 100, 1))
    dmg = [calculate(HP, FM, W, B)[0] for HP in range(10, 100, 1)]

    fig, ax = plt.subplots()
    ax.plot(samples, dmg)

    ax.set(xlabel='sample (s)', ylabel='std attack', title='Wintertodt')
    ax.grid()

    plt.show()


if __name__ == '__main__':

    #manual_calculate()
    auto_calculate()

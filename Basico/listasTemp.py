# -*- coding utf-8 -*-


def run (temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += float(temp)

    return sum_of_temps / len(temps)   


if __name__ == "__main__":
    temps = [21, 24, 8, 4, 40, 36]
    average = run(temps)
    print('la temperatura promedio es: {}'.format(average))
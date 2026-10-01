def pattern():
    for i in range(1, 13):
        for j in range(1, 23):
            if(i == 1 or i == 12 or j == 23-(i*2)):
                print('*', end =' ')

            else:
                print(' ', end = ' ')

        print()

pattern()
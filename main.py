import shutil

def g_c(file):
    hada_file = open(file, 'r')
    hada_read = hada_file.read()
    counter = 1
    for i in hada_read:
        if '\n' in i:
            counter = counter + 1

    return counter

print(g_c("hada.txt"))

def longest_game(file):
    hada_file = open(file, "r")
    hada_read = hada_file.read()
    snake_list = hada_read.split()
    return max(snake_list, key=len)

print(longest_game("hada.txt"))

def copy(file):

    shutil.copyfile(file, "hada2.txt")

copy("hada.txt")

def zip(file):
    hada_file = open(file, 'r')
    hada_read = hada_file.read()
    zipp = ''
    counteragain = {}
    hada_read2 = hada_read.replace('\n', '')
    for x in hada_read2:
        if x in counteragain:
            counteragain[x] = counteragain[x] + 1
        else:
            counteragain[x] = 1
    for y in counteragain:
        if counteragain[y] > 1:
            zipp += y + ' ' + str(counteragain[y])+ ' '
            with open('hada2.txt', "w") as snake2:
                snake2.write(zipp)

print(zip('hada.txt'))




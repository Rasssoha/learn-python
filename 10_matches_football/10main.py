def points(games):
    total = 0
    for j in games:
        i = j.split(':')
        if  i[0] > i[1]:
            total +=3
        if i[0] == i[1]:
            total +=1
        if i[0] < i[1]:
            total +=0
    return total

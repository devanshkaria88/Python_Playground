def solution(xs):
    product = 1
    poslist = []
    neglist = []
    for i in xs:
        if i > 0:
            poslist.append(i)
        elif i < 0:
            neglist.append(i)
    if len(neglist)%2!=0:
        neglist.remove(max(neglist))
        poslist.extend(neglist)
    else:
        poslist.extend(neglist)
    for i in poslist:
        product *= i
    return product

print(solution([5,6,7,-8,-6,-3]))
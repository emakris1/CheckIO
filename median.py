def checkio(data):
    data.sort()
    dlen = len(data)
    index = dlen / 2

    #even length list
    if dlen % 2 == 0:
        median = (data[index] + data[index-1]) / 2.0

    #odd length list
    if dlen % 2 == 1:
        median = data[index]

    return median

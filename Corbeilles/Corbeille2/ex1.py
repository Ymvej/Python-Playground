def convertTime(sec):
    s = sec
    smem = sec
    m = 0
    h = 0
    v = 0

    h = s / 3600
    s = s - (round(h) * 3600)
    m = s / 60
    s = s - (round(m) * 60)
    h = round(h)
    m = round(m)
    s = round(s)

    print(h,':',m,':',s)

    
convertTime
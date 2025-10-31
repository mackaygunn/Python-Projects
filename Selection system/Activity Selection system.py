interviewlist = [['I1', 8.00, 12,00],
                ['I2', 11.00, 14,00],
                ['I3', 9.00, 10.00],
                ['I4', 10.00, 11.00],
                ['I5', 11.00, 13.00],
                ['I6', 15.00, 16.00]]

def selectedinterviews(interviewlist):
    interviewlist.sort(key= lambda x: x[2])

    selected = 0
    first = interviewlist[selected][0]
    print(first)

    for interviews in range(len(interviewlist)):
        if interviewlist[interviews][1] >= interviewlist[selected][2]:
            selected = interviews
            print(interviewlist[selected][0])



selectedinterviews(interviewlist)










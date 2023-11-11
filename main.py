figure = {
    'top-L':"0 ",'top-M':'0 ','top-R': '0 ',
    'mid-L':'x ','mid-M': ' x','mid-R':' ',
    'low-L':' ','low-M':' ','low-R':'x'
}
def Board(borad):
    print(borad['top-L']+'|'+borad['top-M']+'|'+borad['top-R'])
    print('-+-+-')
    print(borad['mid-L']+'|'+borad['mid-M']+'|'+borad['mid-R'])
    print('-+-+-')
    print(borad['low-L']+'|'+borad['low-M']+'|'+borad['low-R'])
Board(figure)


print('md saifulla bin harun\n18 year odl\nhcs examitar\ncomilla')
print('md saifulla bin harun\t18 year odl\thcs examitar\tcomilla')
print('md saifulla bin harun\"18 year odl\"hcs examitar\"comilla')
print('md saifulla bin harun\\18 year odl\\hcs examitar\\comilla')
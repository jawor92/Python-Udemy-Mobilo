
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

while = True:
    try:
        fly1 = ((start, stop) for start in ports for stop in ports if start != stop)
    except:
        StopIteration: 'all were used'
        break
def solution(data, ext, val_ext, sort_by):
    data_rows = ['code', 'date', 'maximum', 'remain']
    res = []
    for row in data :
        if row[data_rows.index(ext)] < val_ext :
            res.append(row)
    
    res = sorted(res, key = lambda  x : x[data_rows.index(sort_by)])
    
    return res
    
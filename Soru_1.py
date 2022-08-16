l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

lnew= []
for i in l:
    if type(i) != list:
        lnew.append(i)
    else:
        for i2 in i:
            if type(i2) != list:
                lnew.append(i2)
            else:
                for i3 in i2:
                    if type(i3) != list:
                        lnew.append(i3)
                    else:
                        for i4 in i3:
                            if type(i4) != list:
                                lnew.append(i4)
        
            
print(lnew)
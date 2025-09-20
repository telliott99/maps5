'''
Just trying this out, try to predict which tile we need
for a given point p.x, p.y and zoom z
'''

def which_tile(x,y,z):
    x += 180
    y = 90-y
    n = 2**z 
       
    # LON
    f = x/360
    print('fx:',f)
    X = int(f*n)
    
    #LAT
    f = y/180
    print('fy:',f)
    Y = int(f*n)
    return X,Y

print(which_tile(-79.94,32.66,10))

def triangles(size):
    for r in range(1,size+1):
        for c in range(1,r+1):
            print('T',end="")
        print()
    for r in range(size-1,0,-1):
        for c in range(1,r+1):
            print('T',end="")
        print()

triangles(6)

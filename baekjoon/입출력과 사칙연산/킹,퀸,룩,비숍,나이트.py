# a, b, c, d, e, f = input().split()
a, b, c, d, e, f = map(int,input().split())
dict = {"king":1,"queen":1,"bishop":2,"knight":2,"rook":2,"pawn":8 }
print(dict["king"]-a, end=' ')
print(dict["queen"]-b, end=' ')
print(dict["bishop"]-c, end=' ')
print(dict["knight"]-d, end=' ')
print(dict["rook"]-e, end=' ')
print(dict["pawn"]-f,)
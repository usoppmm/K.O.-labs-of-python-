class Dot:
    def __init__(self, *coordinates): # конструктор в питоне, self - сам обьект в момент его создания, второе аргументы переданные классу
        self.coordinates = coordinates #A

    def __str__(self):
        return ",".join(map(str, self.coordinates)) #join вставляет разделитель
        #map применяет функцию к каждому элементу списка

    def distance(self, other):
        if not len(self.coordinates) == len(other.coordinates):#B
            raise ValueError
        return sum((a-b)**2 for a,b in zip(self.coordinates, other.coordinates))**0.5 #AB = √(xb - xa)**2 + (yb - ya)**2 + (zb - za)**2

    def middle(self, other):
        if not len(self.coordinates) == len(other.coordinates):
            raise ValueError
        return Dot(*((a+b)/2.0 for a,b in zip(self.coordinates, other.coordinates)))






for A,B in (Dot(1,2,3),Dot(3,4,5)), (Dot(1,2),Dot(3)):
    print (A)
    try:
        print ("{:.3f}".format(A.distance(B)))
        print (A.middle(B))
    except ValueError:
       print ("ERROR")

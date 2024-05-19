from MyWord import cut
import copy
class Polynom:
    def __init__(self):
        self.__data={}
    def _proces_line(self, line):
        rec = cut(line)
        if len(rec) > 0:
            try:
                assert len(rec) == 2
            except:
                return
            try:
                pwd = int(rec[0])
                assert pwd >= 0
            except:
                #print("wrong pover", rec[0])
                return
            try:
                coef = float(rec[1])
            except:
                #print("wrong coef", rec[1])
                return
            try:
                assert pwd not in self.__data
            except:
                return
            self.__data[pwd] = coef

    def read_polynome_from_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                self._proces_line(line)
        if len(self.__data) == 0:
            self.__data[0] = 0.0

    def from_line(self):
        print("empty line to stop")
        while True:
            line=input()
            if len(cut(line))<=1 or cut(line)[0]=='':
                if len(self.__data) == 0:
                    self.__data[0] = 0.0
                return
            else:
                self._proces_line(line)

    def point_in_polinom(self, x):
        res=0.0
        for pwd, coef in self.__data.items():
            res+=x**pwd * coef
        return res
    def get_data(self):
        return self.__data

    def set_data(self, data_list):
        self.__data=copy.copy(data_list)

    def add(self, p1, p2):
        data1=p1.get_data()
        data2=p2.get_data()
        new_data={}
        for pw in set(data1.keys()) | set(data2.keys()):
            new_data[pw]=data1.get(pw, 0.0) + data2.get(pw, 0.0)
        self.set_data(new_data)
    def substract(self, p1, p2):
        data1=p1.get_data()
        data2=p2.get_data()
        new_data={}
        for pw in set(data1.keys()) | set(data2.keys()):
            new_data[pw]=data1.get(pw, 0.0) - data2.get(pw, 0.0)
        self.set_data(new_data)

    def multiply(self, p1, p2):
        data1 = p1.get_data()
        data2 = p2.get_data()
        new_data = {}
        for pw1 in set(data1.keys()) | set(data2.keys()):
            for pw2 in set(data1.keys()) | set(data2.keys()):
                new_data[pw1 + pw2] = data1.get(pw1, 0.0) * data2.get(pw2, 0.0) + new_data.get(pw1+pw2, 0.0)
                if new_data[pw1 + pw2] == 0.0:
                    del new_data[pw1 + pw2]
        self.set_data(new_data)
    def show(self):
        assert len(self.__data)>0
        print(self.__data)

if __name__=="__main__":
    p1=Polynom()
    p2=Polynom()
    p1.read_polynome_from_file('input01.txt')
    p2.read_polynome_from_file('input02.txt')
    d1=Polynom()
    d2=Polynom()
    d3=Polynom()
    d4=Polynom()
    h=Polynom()
    q=Polynom()
    d1.multiply(p2, p1)

    d1.show()

    d2.add(d2, p1)
    q.substract(d2, p2)
    d3.substract(p1, p2)
    d4.multiply(d3, d3)
    h.multiply(p2, d4)
    x=None
    while True:
        try:
            x=float(input())
            break
        except:
            print("please, give corect datas")
    qx=q.point_in_polinom(x)
    hx=h.point_in_polinom(x)
    with open('output.txt', "at") as f:
        print(qx, file=f)
        print(hx, file=f)
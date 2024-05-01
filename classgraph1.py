class Peta:
    def __init__(self):
        self.adj_list = {}

    def addkota(self, kota):
        if kota not in self.adj_list:
            self.adj_list[kota] = [] #menambahkan list nama kota 

    def addjalan(self, kota1, kota2):
        if kota1 in self.adj_list and kota2 in self.adj_list:
            #masukkan kota 1  dilist ke kota2
            self.adj_list[kota1].append(kota2) 
            #masukkan kota 2 dilist ke kota 1
            self.adj_list[kota2].append(kota1)  
            return True
        return False

    def printpeta(self):
        for kota in self.adj_list:
            print(kota, ":", self.adj_list[kota]) 

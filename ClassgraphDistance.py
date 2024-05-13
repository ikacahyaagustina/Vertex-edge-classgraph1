class Peta: 
    def __init__(self): 
        self.adj_list = {} 
 
    def addkota(self, kota):
        if kota not in self.adj_list: 
            self.adj_list[kota] = {} #menambahkan list nama kota  
 
    def addjalan(self, kota1, kota2, distance): 
        if kota1 in self.adj_list and kota2 in self.adj_list: 
            #masukkan kota 1  dilist ke kota2 
            self.adj_list[kota1][kota2] = distance 
            #masukkan kota 2 dilist ke kota 1 
            self.adj_list[kota2][kota1] = distance 
            return True 
        return False 
 
 def printpeta(self): 
        for kota in self.adj_list: 
            print(kota, ":", self.adj_list[kota])  
            for neighbor, distance in self.adj_list[kota].items(): 
                print("     ->", neighbor, ":", distance)

# Tambah vertex (nama kota)
graph.addkota('Surabaya')
graph.addkota('Semarang')
graph.addkota('Jakarta')
graph.addkota('Lampung')
graph.addkota('Jambi')
graph.addkota('Riau')
graph.addkota('Kepulauan Riau')
graph.addkota('Medan')
graph.addkota('Kalimantan Barat')
graph.addkota('Kalimantan Timur')
graph.addkota('Sulawesi Utara')
graph.addkota('Maluku')
graph.addkota('Makassar')
graph.addkota('Papua Barat')

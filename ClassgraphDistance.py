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
graph.addkota('Nusa Tenggara Timur')
graph.addkota('Bali')

# Tambah edge (garis hubungan antar kota)
graph.addjalan('Surabaya', 'Semarang', 653)
graph.addjalan('Surabay', 'Bali', 123)
graph.addjalan('Semarang', 'Jakarta', 234)
graph.addjalan('Semarang', 'Surabaya', 658)
graph.addjalan('Jakarta', 'Lampung', 384)
graph.addjalan('Jakarta', 'Kalimantan Timur', 375)
graph.addjalan('Lampung', 'Jambi', 192)
graph.addjalan('Jambi', 'Riau', 298)
graph.addjalan('Riau', 'Kepulauan Riau', 355)
graph.addjalan('Riau', 'Medan', 423)
graph.addjalan('Kepulauan Riau', 'Medan', 548)
graph.addjalan('Kepulauan Riau', 'Sulawesi Utara', 458)
graph.addjalan('Medan', 'Kalimantan Barat', 673) 
graph.addjalan('Medan', 'Lampung', 383) 
graph.addjalan('Kalimantan Barat', 'Kalimantan Timur', 367) 
graph.addjalan('Kalimantan Barat', 'Riau', 236) 
graph.addjalan('Kalimantan Timur', 'Kepulauan Riau', 294) 
graph.addjalan('Kalimantan Timur', 'Sulawesi Utara', 385) 
graph.addjalan('Sulawesi Utara', 'Maluku', 456) 
graph.addjalan('Sulawesi Utara', 'Papua Barat', 789) 
graph.addjalan('Maluku', 'Makassar', 345) 
graph.addjalan('Maluku', 'Bali', 466) 
graph.addjalan('Maluku', 'Jambi', 658) 
graph.addjalan('Makassar', 'Papua barat', 457) 
graph.addjalan('Makassar', 'Jakarta', 459) 
graph.addjalan('Papua Barat', 'Nusa Tenggara Timur', 578) 
graph.addjalan('Papua barat', 'Kalimantan Barat', 288) 
graph.addjalan('Nusa Tenggara Timur', 'Maluku', 455) 
graph.addjalan('Nusa Tenggara Timur', 'Bali', 127) 
graph.addjalan('Bali', 'Surabaya', 111) 
graph.addjalan('Bali', 'Makasar', 243) 
graph.addjalan('Bali', 'Jakarta', 544) 

# Tampilkan graf (hubungan antar kota)
graph.printpeta()

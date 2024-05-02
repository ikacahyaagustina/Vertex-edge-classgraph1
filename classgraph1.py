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

#contoh penggunaan:
if __name__ == "__main__":
    graph = Peta()

    #tambah vertex (nama kota)
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

    #tambah edge (garis hubungan antar kota)
    graph.addjalan('Surabya', 'Semarang')
    graph.addjalan('Surabaya', 'Bali')
    graph.addjalan('Semarang', 'Jakarta')
    graph.addjalan('Semarang', 'Surabaya')
    graph.addjalan('Jakarta', 'Lampung')
    graph.addjalan('Jakarta', 'Kalimantan Timur')
    graph.addjalan('Lampung', 'Jambi')
    graph.addjalan('Jambi', 'Riau')
    graph.addjalan('Riau', 'Kepulauan Riau')
    graph.addjalan('Kepulauan Riau', 'Medan')
    graph.addjalan('Kepulauan Riau', 'Sulawesi Utara')
    graph.addjalan('Medan', 'Kalimantan Barat')
    graph.addjalan('Medan', 'Lampung')

class artigo:

    def _init_(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def getArtigo(self):
        return f"Titulo:  { self.titulo } |   Autor:   {self.autor}"

class edição:
    def _init_(self, num, vol, data):
        self.num = num
        self.vol = vol
        self.data = data

        self.artigos = []

    def addNartigo(self, artigo):
        self.artigos.append(artigo)

    def getEdição(self):
        return f"Edição numero:  {str(self.num)} | Volume: {str(self.vol)} | Data: {str(self.data)}"

    def ShowArtigo(self):
        for artigo in self.artigos:
            print(artigo.getArtigo())
        
    def getNArtigo(self):
        return len(self.artigos)

    def __getApa_artigo__(self, titulo):
        for artigo in self.artigos:
            if artigo.titulo == titulo:
                self.artigos.remove(artigo)

class revista:
    def _init_(self, titulo, ISSN, periodicidade):
        self.titulo = titulo
        self.ISSN = ISSN
        self.periodicidade = periodicidade
        self.edições = []

    def add_edição(self,edicao):
        self.edição.append(edicao)

    def Publi_Edição(self, edição):
        NArtigo = edição.getNArtigo()
        if(NArtigo >= 10 and NArtigo <= 15):
            self.edições.append(edição)
            return f"Edição lançada com sucesso"
        else:
            return f"É necessario no minimo 10 artigos e nom maximo 15 artigos"

    def ShowEdições(self):
        for edição in self.edições:
            print(edição.getEdição)
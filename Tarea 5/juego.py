from Array2D import Array2D
class JuegoDeLaVida:
    CELULA_VIVA = 1
    CELULA_MUERTA = 0

    def _init_ (self, rens, cols, generaciones, poblacion):
        self.largo = cols
        self.alto = rens
        self.grid = Array2D ( self.alto, self.largo)
        self.grid.clearing(self.CELULA_MUERTA) #TODAS MUERTAS
        self.generaciones = generaciones
        self.poblacion_inicial = poblacion

    def configura_generacion(self,nueva_poblacion):
            self.grid.clearing()
            for celula in nueva_poblacion:
                self.grid.set_item(celula[0],celula[1],self._CELULA_VIVA)

    #Método Grid, colorea la matriz
    def imprime_grid(self):
            for r in range(self.grid.get_num_rows()):
                for c in range (self.grid.get_num_cols()):
                    if self.grid.get_item(r,c) == 0:
                        print("░░",end="")
                    else:
                        print("▓▓",end="")
                print("")

    def get_num_rows(self):
            return  self.alto

    def get_num_cols(self):
            return self.largo

    def set_celula_muerta(self,row,col):
            self.grid.set_item(row,col,self.CELULA_MUERTA)

    def set_celula_viva(self,row,col):
            self.grid.set_item(row,col,self.CELULA_VIVA)

    def get_is_viva(self,row,col):
            return self.grid.get_item(row,col) == self.CELULA_VIVA

    def get_is_muerta(self,row,col):
            return self.grid.get_item(row,col) == self.CELULA_MUERTA


    #Meodo para saber y limitar el número de vecinos
    def get_numero_vecinos_vivos(self,row,col):
            limites = [row-1 , row+1 , col-1 , col+1]
            vivos = 0
            limites = self._ajusta_limites_(limites)
            if row >= 0 and row <=self.alto-1 and col >=0 and col <= self.largo-1:
                for r in range(limite[0], limites[1]+1):
                    for c in range (limites [2],limites[3]+1):
                        if r == row and c == col:
                            continue
                        else:
                            if self.grid.get_item(r,c) == CELULA_VIVA:
                                vivos += 1
            else:
                print("Coordenada la celula fuera del grid")
            return vivos

    def evolucionar(self):
        grid = self.grid
        for i in range(grid.get_num_rows()):
            for j in range(grid.get_num_cols()):
                # Una celula que no tiene vecinos vivos o que tiene solo un vecino vivo, muere por soledad.
                if (grid.get_item(r, c) == 1 and self.get_numero_vecinos_vivos(r, c) < 2):

                    # Una celula viva que tiene cuatro o mas vecinos vivos, muere por sobrepoblación
                elif (grid.get_item(r, c) == 1 and self.get_numero_vecinos_vivos(r, c) >= 4):

                    # Una celula muerta con exactamente tres vecinos vivos, resulta en un nacimiento
                elif (grid.get_item(r, c) == 0 and self.get_numero_vecinos_vivos(r, c) == 3):

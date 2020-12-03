from backtracking import LaberintoADT
pasillos_inicial = ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
entrada = (5,2)
salida = (2,5)
lab = LaberintoADT(6, 6, pasillos_inicial, entrada, salida)
lab.to_string()

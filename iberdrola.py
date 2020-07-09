import csv

def convertir_csv (fichero):

    csv_reader = csv.reader(fichero, delimiter=';')
    line_count = 0
    salida =""
    linea = ""
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            #print ('CUPS,	Fecha,	Hora ,Consumo_kWh	,Metodo_obtencion')
             salida='CUPS,	Fecha,	Hora ,Consumo_kWh	,Metodo_obtencion'
             line_count += 1
        else:
            Kw = float(row[3])/1000
            #print (Kw)
            
            Fecha_Hora = row[1]
            # Ajustamos la Hora
            Hora = Fecha_Hora[10:13]
            Hora24 = int(Hora)+ 1
            #print(Hora24)
            # Ajustamos la Fecha 

            #Fecha = Fecha_Hora[:10]# Fecha YYYY/MM/DD
            Fechaddmmaa = Fecha_Hora[8:10]+"/"+Fecha_Hora[5:7]+"/" +Fecha_Hora[:4]
            #print (Fechaddmmaa)

            
            linea = f'\n{row[0]},{Fechaddmmaa}, {Hora24},{Kw},R'
            #salida.append (linea)
            salida =salida + linea
          
            #print (f'\t{row[0]},{Fechaddmmaa}, {Hora24},{Kw},R')
            line_count += 1
   # print(f'Processed {line_count} lines.')            
      
    print (salida)
    return (salida) 
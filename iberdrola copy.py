import csv
'''
*with open('./name.csv') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:   
              print(row)       
              #print(row['CUPS'], row['FECHA-HORA'])

'''
'''
with open('name.csv') as File:
    reader = csv.reader(File, delimiter=';', quotechar=';',
                        quoting=csv.QUOTE_MINIMAL)
    
    
    
    n=0
    for row in reader:
       if n==0:
            n=n+1
       else:    
            print(row)              
'''
import csv
import datetime

with open('name.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
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

            Fecha = Fecha_Hora[:10]# Fecha YYYY/MM/DD
            Fechaddmmaa = Fecha_Hora[8:10]+"/"+Fecha_Hora[5:7]+"/" +Fecha_Hora[:4]
            #print (Fechaddmmaa)

            
            linea = f'\n{row[0]},{Fechaddmmaa}, {Hora24},{Kw},R'
            #salida.append (linea)
            salida =salida + linea
          
            #print (f'\t{row[0]},{Fechaddmmaa}, {Hora24},{Kw},R')
            line_count += 1
   # print(f'Processed {line_count} lines.')            
      
    print (salida) 
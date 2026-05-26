
import pandas as pd

#sudo apt install python3-pip
#pip3 install pandas
#Tecnica@UBA
df=pd.read_csv("2024_medalists_all.csv")
#Defino una variable en esa variable carga todo mi archivo

print("OKEY! Archivo cargado correctamente")
#Muestra si carga bien el programa 

# Mostrando las primeras filas del dataframe
print(df.head())

#resultado = df [df['medalist_name'] == 2024]

#total_medalist =df['medalist_name'].count()
#esta contando todos los nombres 

total_medalist =df['medalist_name'].sum()

print(f"Total de registros:{total_medalist}")
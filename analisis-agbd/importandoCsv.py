import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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

#total_medalist =df['medalist_name'].sum()

#print(f"Total de registros:{total_medalist}")

filtro_avanzado= df["event_name"].str.startswith("athletics", na=False)
df_filtrado= df[filtro_avanzado]
sum_latitud=df_filtrado["lat"].sum()

#print("----reporte----")
print (f"Monto analizado:USD {sum_latitud:.2f} millones")
df['Inversion_USD'] = 25000

#condicional

if default_limite_alto:= (sum_latitud > 5000):
    print ("¡Alerta! El monto total supera lo establecido.")
    print("Requiere revision inmediata")

elif sum_latitud < 1000:
   print("Aviso: mercado moderado/alto")
   print("Monitorear comportamiento prox trim")
else:
    print("Mercado estable, sin alertas por el momento.")


#Grafico de barras usando toda DF
print("\n [Generando GRAFICO de barras]")

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,6))
sns.barplot(
    data=df,
    x="event_name",
    y="lat",
    estimator=sum,
    errorbar=None,
    palette="viridis",
)
plt.title("Comparativa de Mercado por tipo de Hardware",fontsize= 14)
plt.xticks(rotation=20)

#Guiardo grafico generado
plt.savefig ("grafico_barra.png", dpi=300)
plt.close




#hice un reporte financiero básico: ¿Cuánto se gastó por género?
#eporte_genero = df['sex_or_gender'].str.startswith('female', na = False)
#df_genero = df[reporte_genero]
#sum_dinero = df_genero['Inversion_USD'].sum()

#print("--- REPORTE TOTAL DE INVERSIÓN POR GÉNERO ---")
#print(reporte_genero)
#print(sum_dinero)
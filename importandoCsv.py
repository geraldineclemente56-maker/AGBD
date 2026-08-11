import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

#sudo apt install python3-pip
#pip3 install pandas
#Tecnica@UBA

df=pd.read_csv("2024_medalists_all.csv")
#print(f'Archivo exportado: {len(df_filtrado)} filas guardadas.')


#Defino una variable en esa variable carga todo mi archivo
plt.close('all')
print("OKEY! Archivo cargado correctamente")
#Muestra si carga bien el programa 

# Mostrando las primeras filas del dataframe
print(df.head())
agrupado = df.groupby('event_name')['lat'].sum().sort_values()
plt.xticks()  
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(agrupado.index, agrupado.values, marker='o',
 color='#2E75B6', linewidth=2, markersize=8)
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

if limite_alto:= (sum_latitud > 5000):
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
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x="sex_or_gender",
    hue="sex_or_gender",
    legend=False,
    palette="viridis",
)


plt.title("Total de Medallistas por Género (París 2024)", fontsize=14)
plt.xlabel("Género")
plt.ylabel("Cantidad de Medallistas")
plt.tight_layout()
plt.savefig("grafico_barra_genero.png", dpi=300)
#plt.show()
plt.close()

print("\n[Generando GRÁFICO de líneas]")
agrupado = df.groupby("event_name")["Inversion_USD"].sum().head(10)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    agrupado.index,
    agrupado.values,
    marker="o",
    color="#2E75B6",
    linewidth=2,
    markersize=8,
)
ax.set_title('Deportes por cantidad de medallas(TOP 10)', fontsize=14, fontweight='bold')
ax.set_xlabel('Deporte')
ax.set_ylabel('Total de medallas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('grafico_lineas.png', dpi=150)
#plt.show()
plt.close()

filtro_avanzado = (df["sex_or_gender"] == "female") & (df["lat"] > 40.0)
resultado_original = df[filtro_avanzado]


limite_latitud = 40.0
resultado_query = df.query(
    'sex_or_gender == "female" and lat > @limite_latitud'
)


print("Con corchetes:")
print(resultado_original)

print("\nCon .query():")
print(resultado_query)

print("\n¿Son iguales?", resultado_original.equals(resultado_query))



categorias_elegidas = ["female"]

df_incluidos = df[df["sex_or_gender"].isin(categorias_elegidas)]
df_excluidos = df[~df["sex_or_gender"].isin(categorias_elegidas)]

print(f"Filas incluidas ({len(df_incluidos)}):")
print(df_incluidos)
print(f"\nFilas excluidas ({len(df_excluidos)}):")
print(df_excluidos)

total = len(df)
suma = len(df_incluidos) + len(df_excluidos)
print(f"\nTotal original: {total}  |  Incluidos + Excluidos: {suma}")
print(f"¿Coinciden? {total == suma}")

print("=== DataFrame completo ===")
print(df["sex_or_gender"].value_counts())
print("Valores únicos:", df["sex_or_gender"].unique())
print("Cantidad de categorías:", df["sex_or_gender"].nunique())
print("Porcentajes:")
print((df["sex_or_gender"].value_counts(normalize=True) * 100).round(1))


df_filtrado = df[filtro_avanzado]

print("\n=== DataFrame filtrado ===")
print(df_filtrado["sex_or_gender"].value_counts())
print("Valores únicos:", df_filtrado["sex_or_gender"].unique())
print("Cantidad de categorías:", df_filtrado["sex_or_gender"].nunique())
print("Porcentajes:")
print(
    (df_filtrado["sex_or_gender"].value_counts(normalize=True) * 100).round(1)
)

#hice un reporte financiero básico: ¿Cuánto se gastó por género?
#eporte_genero = df['sex_or_gender'].str.startswith('female', na = False)
#df_genero = df[reporte_genero]
#sum_dinero = df_genero['Inversion_USD'].sum()

#print("--- REPORTE TOTAL DE INVERSIÓN POR GÉNERO ---")
#print(reporte_genero)
#print(sum_dinero)
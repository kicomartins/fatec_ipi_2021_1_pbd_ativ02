import numpy as np
import matplotlib as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv(r'C:\Users\rrama\Documents\FATEC IPIRANGA\2021-1º Sem\Programação para Banco de Dados\04_dados_exercicio.csv')
features = dataset.iloc[:, :4].values
classe = dataset.iloc[:, -1].values
print (features)
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(features[:, ])
columnTransformer = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
features = np.array(columnTransformer.fit_transform(features))
labelEncoder = LabelEncoder()
classe = labelEncoder.fit_transform(classe)
print('=============features==============')
print(features)
print('=============classe==============')
print(classe)
features_treinamento, features_teste, classe_treinamento, classe_teste = train_test_split(features, classe, test_size = 0.15, random_state=1)
print('=============features_treinamento==============')
print(features_treinamento)
print('=============features_teste==============')
print(features_teste)
print('=============classe_treinamento==============')
print(classe_treinamento)
print('=============classe_teste==============')
print(classe_teste)
standardScaler = StandardScaler()
features_treinamento[:, 3:] = standardScaler.fit_transform(features_treinamento[:, 3:])
features_teste[:, 3:] = standardScaler.transform(features_teste[:, 3:])
print('=============features_treinamento==============')
print(features_treinamento)
print('=============features_teste==============')
print(features_teste)
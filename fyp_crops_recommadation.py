import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.neighbors import KNeighborsClassifier 

excel_data = pd.read_excel('datset.xlsx', header = 0)
print(excel_data)                                                              
print(excel_data.shape)    

labels = preprocessing.LabelEncoder()
crop = labels.fit_transform(list(excel_data["CROP"]))

PH = list(excel_data["PH"])
MOISTURE = list(excel_data["MOISTURE"])
HUMIDITY = list(excel_data["HUMIDITY"])
TEMPERATURE =list(excel_data["TEMPERATURE"])

features = list(zip(PH, MOISTURE, HUMIDITY, TEMPERATURE))
features = np.array([PH, MOISTURE, HUMIDITY, TEMPERATURE])

features = features.transpose()
print(features.shape)                                                                                          # Printing the shape of the features after getting transposed.
print(crop.shape)

model = KNeighborsClassifier(n_neighbors=8)
model.fit(features, crop)

prediction = np.array([30,0,30,4])
print(prediction)
prediction = prediction.reshape(1,-1)
print(prediction)
prediction = model.predict(prediction)
print(prediction)


crop_name = str()
if prediction == 0:                                                                                              # Above we have converted the crop names into numerical form, so that we can apply the machine learning model easily. Now we have to again change the numerical values into names of crop so that we can print it when required. 
    crop_name = 'Apple(सेब)'
elif prediction == 1:
    crop_name = 'Banana(केला)'
elif prediction == 2:
    crop_name = 'Blackgram(काला चना)'
elif prediction == 3:
    crop_name = 'Chickpea(काबुली चना)'
elif prediction == 4:
    crop_name = 'Coconut(नारियल)'
elif prediction == 5:
    crop_name = 'Coffee(कॉफ़ी)'
elif prediction == 6:
    crop_name = 'Cotton(कपास)'
elif prediction == 7:
    crop_name = 'Grapes(अंगूर)'
elif prediction == 8:
    crop_name = 'Jute(जूट)'
elif prediction == 9:
    crop_name = 'Kidneybeans(राज़में)'
elif prediction == 10: 
    crop_name = 'Lentil(मसूर की दाल)'
elif prediction == 11:
    crop_name = 'Maize(मक्का)'
elif prediction == 12:
    crop_name = 'Mango(आम)'
elif prediction == 13:
    crop_name = 'Mothbeans(मोठबीन)'
elif prediction == 14:
    crop_name = 'Mungbeans(मूंग)'
elif prediction == 15:
    crop_name = 'Muskmelon(खरबूजा)'
elif prediction == 16:
    crop_name = 'Orange(संतरा)'
elif prediction == 17:
    crop_name = 'Papaya(पपीता)'
elif prediction == 18:
    crop_name = 'Pigeonpeas(कबूतर के मटर)'
elif prediction == 19:
    crop_name = 'Pomegranate(अनार)'
elif prediction == 20:
    crop_name = 'Rice(चावल)'
elif prediction == 21:
    crop_name = 'Watermelon(तरबूज)'

print(crop_name)
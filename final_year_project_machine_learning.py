import pyttsx3                                                            # Importing pyttsx3 library to convert text into speech.
import pandas as pd                                                       # Importing pandas library
from sklearn import preprocessing                                         # Importing sklearn library. This is a very powerfull library for machine learning. Scikit-learn is probably the most useful library for machine learning in Python. The sklearn library contains a lot of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction.
from sklearn.neighbors import KNeighborsClassifier                        # Importing Knn Classifier from sklearn library.
import numpy as np                                                        # Importing numpy to do stuffs related to arrays
import PySimpleGUI as sg                                                  # Importing pysimplegui to make a Graphical User Interface.

excel = pd.read_excel('datset.xlsx', header = 0)                            # Importing our excel data from a specific file.
print(excel)                                                              # Printing our excel file data.
print(excel.shape)                                                        # Checking out the shape of our data.

engine = pyttsx3.init('sapi5')                                            # Defining the speech rate, type of voice etc.
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
engine.setProperty('voice',voices[0].id)


def speak(audio):                                                         # Defining a speak function. We can call this function when we want to make our program to speak something.
	engine.say(audio) 
	engine.runAndWait()

le = preprocessing.LabelEncoder()                                         # Various machine learning algorithms require numerical input data, so you need to represent categorical columns in a numerical column. In order to encode this data, you could map each value to a number. This process is known as label encoding, and sklearn conveniently will do this for you using Label Encoder.
crop = le.fit_transform(list(excel["CROP"]))  

PH = list(excel["PH"])
MOISTURE = list(excel["MOISTURE"])
HUMIDITY = list(excel["HUMIDITY"])
TEMPERATURE = list(excel["TEMPERATURE"])



features = list(zip(PH, MOISTURE, HUMIDITY, TEMPERATURE))
features = np.array([PH, MOISTURE, HUMIDITY, TEMPERATURE])

features = features.transpose()                                                                                # Making transpose of the features 
print(features.shape)                                                                                          # Printing the shape of the features after getting transposed.
print(crop.shape)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(features, crop)
layout = [[sg.Text('                      Crop Recommendation Assistant', font=("Helvetica", 30), text_color = 'yellow')],                                                    # Defining the layout of the Graphical User Interface. It consist of some text, Buttons, and blanks to take Input.                                                        
         [sg.Text('Please enter the following details :-', font=("Helvetica", 20))],
         [sg.Text('Enter ratio of PH                               :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1))],
         [sg.Text('Enter Moisture        :', font=("Helvetica", 20)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('*C', font=("Helvetica", 20))],                                                                                           # We have defined the text size, font type, font size, blank size, colour of the text in the GUI.
         [sg.Text('Enter Humidity                                  :', font=("Helvetica", 20)), sg.Input(font=("Helvetica",20), size = (20,1) )],
		 [sg.Text('Enter ratio Temperature                                  :', font=("Helvetica", 20)), sg.Input(font=("Helvetica",20), size = (20,1) )],
		 [sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'yellow', key='-OUTPUT1-' )],
         [sg.Button('Submit', font=("Helvetica", 20)),sg.Button('Quit', font=("Helvetica", 20))] ]
window = sg.Window('Crop Recommendation Assistant', layout) 

while True: 
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Quit':                                                                                            # If the user will press the quit button then the program will end up.
		break
	print(values[0])
	ph_content =         values[0]                                                                                                        # Taking input from the user about nitrogen content in the soil.
	moisture_content =       values[1]                                                                                                        # Taking input from the user about phosphorus content in the soil.
	humidity_content =        values[2]                                                                                                        # Taking input from the user about potassium content in the soil.
	temperature_content =      values[3]
	predict1 = np.array([ph_content,humidity_content,temperature_content,moisture_content,])
	print(predict1)
	predict1 = predict1.reshape(1,-1)                                                                              # Reshaping the input data so that it can be applied in the model for getting accurate results.
	print(predict1)                                                                                                # Printing the input data value after being reshaped.
	predict1 = model.predict(predict1)                                                                             # Applying the user input data into the model. 
	print(predict1)     
                                                                                          # Finally printing out the results.
	crop_name = str()
	if predict1 == 0:                                                                                              # Above we have converted the crop names into numerical form, so that we can apply the machine learning model easily. Now we have to again change the numerical values into names of crop so that we can print it when required. 
		crop_name = 'Apple(सेब)'
	elif predict1 == 1:
		crop_name = 'Banana(केला)'
	elif predict1 == 2:
		crop_name = 'Blackgram(काला चना)'
	elif predict1 == 3:
		crop_name = 'Chickpea(काबुली चना)'
	elif predict1 == 4:
		crop_name = 'Coconut(नारियल)'
	elif predict1 == 5:
		crop_name = 'Coffee(कॉफ़ी)'
	elif predict1 == 6:
		crop_name = 'Cotton(कपास)'
	elif predict1 == 7:
		crop_name = 'Grapes(अंगूर)'
	elif predict1 == 8:
		crop_name = 'Jute(जूट)'
	elif predict1 == 9:
		crop_name = 'Papaya(पपीता)'
	elif predict1 == 10:
		crop_name = 'Lentil(मसूर की दाल)'
	elif predict1 == 11:
		crop_name = 'Maize(मक्का)'
	elif predict1 == 12:
		crop_name = 'Mango(आम)'
	elif predict1 == 13:
		crop_name = 'Mothbeans(मोठबीन)'
	elif predict1 == 14:
		crop_name = 'Mungbeans(मूंग)'
	elif predict1 == 15:
		crop_name = 'Muskmelon(खरबूजा)'
	elif predict1 == 16:
		crop_name = 'Orange(संतरा)'
	elif predict1 == 17:
		crop_name = 'Papaya(पपीता)'
	elif predict1 == 18:
		crop_name = 'Pigeonpeas(कबूतर के मटर)'
	elif predict1 == 19:
		crop_name = 'Pomegranate(अनार)'
	elif predict1 == 20:
		crop_name = 'Rice(चावल)'
	elif predict1 == 21:
		crop_name = 'Watermelon(तरबूज)'

	if int(humidity_content) >=1 and int(humidity_content)<= 33 :                                                # Here I have divided the humidity values into three categories i.e low humid, medium humid, high humid.
		humidity_level = 'low humid'
	elif int(humidity_content) >=34 and int(humidity_content) <= 66:
		humidity_level = 'medium humid'
	else:
		humidity_level = 'high humid'

	if int(temperature_content) >= 0 and int(temperature_content)<= 6:                                           # Here I have divided the temperature values into three categories i.e cool, warm, hot.
		temperature_level = 'cool'
	elif int(temperature_content) >=7 and int(temperature_content) <= 25:
		temperature_level = 'warm'
	else:
		temperature_level= 'hot' 

	print(crop_name)
	speak("The best crop that you can grow is  " + crop_name) 

window.close() 
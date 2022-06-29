import pickle
pkl_file = "model.pkl"  
with open(pkl_file, 'rb') as file:  
    pickle_model = pickle.load(file)
new_input = 'i just love south africa'
predictions = pickle_model.predict([new_input])
print(predictions)

#print("Hello world")
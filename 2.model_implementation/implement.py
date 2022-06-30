import pickle
pkl_file = "model.pkl"  
with open(pkl_file, 'rb') as file:  
    pickle_model = pickle.load(file)
new_input = 'Ndiyamthanda uNeloson mandela , ebeyindoda yonyaka. ungathethi kakubi ngaye. Utata wethu'
predictions = pickle_model.predict([new_input])
print(predictions)

#print("Hello world")
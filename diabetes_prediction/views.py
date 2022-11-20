from django.shortcuts import render
import joblib


global __model
with open('./artifacts/saved_model.pkl', 'rb') as f:
            __model = joblib.load(f)
def home(request):
    return render (request,'home.html')

def predict(request):
    return render (request,'predict.html')

def result(request):
    
    val1=float(request.GET['n1'])
    val2=float(request.GET['n2'])
    val3=float(request.GET['n3'])
    val4=float(request.GET['n4'])
    val5=float(request.GET['n5'])
    val6=float(request.GET['n6'])
    val7=float(request.GET['n7'])
    val8=float(request.GET['n8'])
    pred=__model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    map={
        0:"Negative",
        1:"Positive"
    }
    result1=map[pred[0]]
    return render (request,'predict.html',{"result2":result1})


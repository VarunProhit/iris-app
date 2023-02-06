from django.shortcuts import render
from joblib import load

model = load('./savedModels/model.joblib')
# Create your views here.
def predictor(requests):
    if requests.method == 'POST':
        sepal_length = requests.POST['sepal_length']
        sepal_width = requests.POST['sepal_width']
        petal_length = requests.POST['petal_length']
        petal_width = requests.POST['petal_width']
        y_pred = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        if y_pred==0:
            y_pred='setosa'
        elif y_pred==1:
            y_pred='verscicolor'
        else:
            y_pred='virginica'
        # print(y_pred)
        return render(requests,'main.html',{'result':y_pred})
    return render(requests,'main.html')

# def formInfo(request):
    
#     return render(request,'result.html',{'result':y_pred})
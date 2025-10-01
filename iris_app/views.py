from django.shortcuts import render
from .forms import IrisForm
import joblib
from .ml_model import train_model,predict
def predict_species(request):
    prediction = None  # Store prediction here

    if request.method == "POST":
        form = IrisForm(request.POST)
        if form.is_valid():
            # Extract input values
            data = [
                form.cleaned_data["sepal_length"],
                form.cleaned_data["sepal_width"],
                form.cleaned_data["petal_length"],
                form.cleaned_data["petal_width"],
            ]
            print(data)
            # Make prediction
            model=train_model()
            prediction=predict(model,data)
    else:
        form = IrisForm()  # Empty form for GET request

    return render(request, "predict.html", {"form": form, "prediction": prediction})

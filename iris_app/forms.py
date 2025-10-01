from django import forms


class IrisForm(forms.Form):
    sepal_length=forms.FloatField(label="enter the sepal length")
    sepal_width=forms.FloatField(label="sepal width")
    petal_length=forms.FloatField(label="petal length")
    petal_width=forms.FloatField(label="petal width")

    
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
from .models import IrisModel


def train_model():
    qs=IrisModel.objects.all().values()##return list of dicts
    df=pd.DataFrame(qs)
    X=df.drop(columns=['id','species'])
    y=df['species']


    X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=0.2,random_state=42
    )


    model=LogisticRegression(max_iter=200)
    model.fit(X_train,y_train)


    # joblib.dump(model,"iris_model.pkl")
    accuracy=model.score(X_test,y_test)
    print("model accuracy on test set is",accuracy)

    return model


def predict(model, features):
    """
    model    : trained LogisticRegression model
    features : list of 4 values [sepal_length, sepal_width, petal_length, petal_width]
    """
    # Wrap in list to make 2D
    pred = model.predict([features])
    return pred[0]  # Return predicted species

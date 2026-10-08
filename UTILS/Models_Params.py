
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from xgboost import XGBClassifier

from sklearn.discriminant_analysis import (
    LinearDiscriminantAnalysis,
    QuadraticDiscriminantAnalysis
)

from sklearn.naive_bayes import GaussianNB

from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier


from sklearn.ensemble import(

    RandomForestClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier,
    BaggingClassifier
  )



class Models_Parameters :

    def baseline_params(self):

      

      models = {
                "Logistic Regression": LogisticRegression(),
                "LDA": LinearDiscriminantAnalysis(),
                "QDA": QuadraticDiscriminantAnalysis(),
                "Decision Tree": DecisionTreeClassifier(),
                "Random Forest": RandomForestClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "XGBoost": XGBClassifier(),
                "LightGBM": LGBMClassifier(),
                "CatBoost": CatBoostClassifier(),
                "SVM": SVC(),
                "KNN": KNeighborsClassifier(),
                "Naive Bayes": GaussianNB(),
                "AdaBoost": AdaBoostClassifier(),
                "Bagging": BaggingClassifier()
                 }

      return  models
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))


import pandas as pd
from PROCESSING.DATA_PROCESSING import DataProcessor
from UTILS.Models_Params import Models_Parameters
from PROCESSING.DATA_PROCESSING import DataProcessor

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    balanced_accuracy_score,
    average_precision_score,
    roc_auc_score
)




class BaseLine_Models: 

    def __init__(self, models,df):
        self.models = models
        self.data = df




    def simple_test(self, y_test, y_predict, y_proba, model_name):
    
            metrics = {
                "Model": model_name,
                "Accuracy": round(
                    accuracy_score(y_test, y_predict), 3
                ),
                "Precision": round(
                    precision_score(y_test, y_predict), 3
                ),
                "Recall": round(
                    recall_score(y_test, y_predict), 3
                ),
                "F1": round(
                    f1_score(y_test, y_predict), 3
                ),
                "Balanced Accuracy": round(
                    balanced_accuracy_score(y_test, y_predict), 3
                )
            }
    
            if y_proba is None:
    
                metrics["ROC-AUC"] = None
                metrics["PR-AUC"] = None
    
            else:
    
                metrics["ROC-AUC"] = round(
                    roc_auc_score(y_test, y_proba), 3
                )
    
                metrics["PR-AUC"] = round(
                    average_precision_score(y_test, y_proba), 3
                )
    
            return metrics




    


    def run_all_models(self):

        metrics = []
        
        processor = DataProcessor(self.data)
        
        X_train, X_test, y_train, y_test = processor.process()
        
        for model_name, model in self.models.items():
        
                print(f"Training {model_name}...")
        
                model.fit(X_train, y_train)
        
                y_predict = model.predict(X_test)
        
                if model_name == "SVM":
                    y_score = None
        
                else:
                    y_score = model.predict_proba(X_test)[:, 1]
        
                m = self.simple_test(
                    y_test,
                    y_predict,
                    y_score,
                    model_name
                   )
        
                metrics.append(m)
        
        return pd.DataFrame(metrics)
    

    


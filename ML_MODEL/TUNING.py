
import pandas as pd 

from sklearn.model_selection import (
    StratifiedKFold,
    GridSearchCV,
    RandomizedSearchCV                        
    )




class HyperparameterTuner:

    def __init__(
        self,
        model,
        search_space,
        search_type="grid",
        cv=5,
        scoring={
                "accuracy": "accuracy",
                "precision": "precision",
                "recall": "recall",
                "f1": "f1",
                "roc_auc": "roc_auc"
                },
        n_iter=20,
        n_jobs=-1,
        random_state=42
    ):
        self.model = model
        self.search_space = search_space
        self.search_type = search_type
        self.cv = cv
        self.scoring = scoring
        self.n_iter = n_iter
        self.n_jobs = n_jobs
        self.random_state = random_state
        self.model_name = type(self.model).__name__


    def tune(self, X_train, y_train):

        cv_strategy = StratifiedKFold(
            n_splits=self.cv,
            shuffle=True,
            random_state=self.random_state
        )

        if self.search_type == "grid":

            search = GridSearchCV(
                estimator=self.model,
                param_grid=self.search_space,
                cv=cv_strategy,
                scoring=self.scoring,
                n_jobs=self.n_jobs,
                refit="f1"
            )

        elif self.search_type == "random":

            search = RandomizedSearchCV(
                estimator=self.model,
                param_distributions=self.search_space,
                n_iter=self.n_iter,
                cv=cv_strategy,
                scoring=self.scoring,
                n_jobs=self.n_jobs,
                random_state=self.random_state,
                refit="f1"
            )

        else:

            raise ValueError(
                f"Unknown search_type: {self.search_type}"
            )

        search.fit(X_train, y_train)


        # Preserve the tuning results for later use.
        self.best_params_ = search.best_params_
        self.best_score_ = search.best_score_
        self.best_estimator_ = search.best_estimator_
        self.search_object_ = search



        # Return the model name and best parameters as a DataFrame.
        results_df = pd.DataFrame([
            {
                "Model": self.model_name,
                "Best Params": self.best_params_
            }
        ])





        return results_df
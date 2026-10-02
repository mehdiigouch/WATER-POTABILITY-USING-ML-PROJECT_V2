


import pandas as pd



from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer






class DataProcessor:

    def __init__(
        self,
        data: pd.DataFrame,
        target_col: str = "potability",
        test_size: float = 0.2,
        random_state: int = 42
    ):
        if not isinstance(data, pd.DataFrame):
            raise TypeError("data must be a pandas DataFrame")

        if target_col not in data.columns:
            raise ValueError(
                f"Target column '{target_col}' was not found in the DataFrame."
            )

        if data[target_col].isna().any():
            raise ValueError(
                f"Target column '{target_col}' contains missing values."
            )

        self.df = data.copy()
        self.target_col = target_col
        self.test_size = test_size
        self.random_state = random_state

        self.preprocessor = Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ])




    def process(self):

        # --------------------------------------------------
        # 1. Separate features and target
        # --------------------------------------------------

        X = self.df.drop(columns=self.target_col)
        y = self.df[self.target_col]

        # Keep feature names for the final DataFrames
        feature_names = X.columns.tolist()

        # --------------------------------------------------
        # 2. Split the data
        # --------------------------------------------------

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=y
        )

        # Save indexes so they remain aligned after transformation
        train_index = X_train.index
        test_index = X_test.index

        # --------------------------------------------------
        # 3. Fit preprocessing ONLY on training data
        # --------------------------------------------------

        X_train = self.preprocessor.fit_transform(X_train)

        # --------------------------------------------------
        # 4. Apply learned preprocessing to test data
        # --------------------------------------------------

        X_test = self.preprocessor.transform(X_test)

        # --------------------------------------------------
        # 5. Convert transformed arrays back to DataFrames
        # --------------------------------------------------

        X_train_df = pd.DataFrame(
            X_train,
            columns=feature_names,
            index=train_index
        )

        X_test_df = pd.DataFrame(
            X_test,
            columns=feature_names,
            index=test_index
        )

        # --------------------------------------------------
        # 6. Keep targets as Series
        # --------------------------------------------------

        y_train = y_train.rename(self.target_col)
        y_test = y_test.rename(self.target_col)

        # --------------------------------------------------
        # 7. Return processed data
        # --------------------------------------------------

        return X_train_df, X_test_df, y_train, y_test

    



    
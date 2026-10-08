
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


from scipy.stats import (
    randint,
    loguniform,
    uniform
    
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
    














    def tuning_params(self):


###############################   LOGISTIC REGRESSION #######################################

            logistic_regression_par = [

              # L2 penalty
              {
                  "C": [0.001, 0.005, 0.01, 0.1, 0.5, 1, 5, 10],
                  "max_iter": [500, 1000, 2000],
                  "penalty": ["l2"],
                  "solver": [
                      "lbfgs",
                      "liblinear",
                      "newton-cg",
                      "newton-cholesky",
                      "sag",
                      "saga"
                  ],
                  "fit_intercept": [True, False],
                  "class_weight": [None, "balanced"]
              },

              # L1 penalty
              {
                  "C": [0.001, 0.005, 0.01, 0.1, 0.5, 1, 5, 10],
                  "max_iter": [500, 1000, 2000],
                  "penalty": ["l1"],
                  "solver": [
                      "liblinear",
                      "saga"
                  ],
                  "fit_intercept": [True, False],
                  "class_weight": [None, "balanced"]
              },

              # No regularization
              {
                  "max_iter": [500, 1000, 2000],
                  "penalty": [None],
                  "solver": [
                      "lbfgs",
                      "newton-cg",
                      "newton-cholesky",
                      "sag",
                      "saga"
                  ],
                  "fit_intercept": [True, False],
                  "class_weight": [None, "balanced"]
              },

              # Elastic Net
              {
                  "C": [0.001, 0.005, 0.01, 0.1, 0.5, 1, 5, 10],
                  "max_iter": [500, 1000, 2000],
                  "penalty": ["elasticnet"],
                  "solver": ["saga"],
                  "l1_ratio": [0.1, 0.5, 0.9],
                  "fit_intercept": [True, False],
                  "class_weight": [None, "balanced"]
              }
          ]


########################################   LDA  ###########################################
            

            Linear_Discriminant_Analysis = [
              {
                  "solver": ["svd"],
                  "shrinkage": [None],
                  "n_components": [None, 1],
                  "store_covariance": [False, True],
                  "tol": [1e-4, 1e-3, 1e-2]
              },
              {
                  "solver": ["lsqr"],
                  "shrinkage": [None, "auto"],
                  "n_components": [None, 1],
                  "tol": [1e-4, 1e-3, 1e-2]
              },
              {
                  "solver": ["eigen"],
                  "shrinkage": [None, "auto"],
                  "n_components": [None, 1],
                  "tol": [1e-4, 1e-3, 1e-2]
              }
          ]


##################################   QDA  ##############################################

            Quadratic_Discriminant_Analysis = [
              {
                  "solver": ["svd"],
                  "shrinkage": [None],
                  "reg_param": [0.0, 0.01, 0.05, 0.1, 0.2, 0.5, 0.8, 1.0]
              },
              {
                  "solver": ["eigen"],
                  "shrinkage": [None, "auto"],
                  "reg_param": [0.0, 0.01, 0.05, 0.1, 0.2, 0.5, 0.8, 1.0]
              }
          ]


################################### KNN #####################################################


            KNN_params = {

              # Number of neighbors
              "n_neighbors": randint(3, 31),

              # How neighbors are weighted
              "weights": [
                  "uniform",
                  "distance"
              ],

              # Distance metric
              "metric": [
                  "euclidean",
                  "manhattan",
                  "minkowski"
              ],

              # Power parameter for Minkowski distance
              "p": [1, 2],

              # Algorithm used to find neighbors
              "algorithm": [
                  "auto",
                  "ball_tree",
                  "kd_tree",
                  "brute"
              ],

              # Leaf size used by tree-based algorithms
              "leaf_size": [
                  10,
                  20,
                  30,
                  40,
                  50
              ]
          }


                  
########################################### SVM #################################################


            SVM_params = {

                # Regularization
                "C": loguniform(0.01, 100),

                # Kernel function
                "kernel": [
                    "linear",
                    "rbf",
                    "poly",
                    "sigmoid"
                ],

                # Kernel coefficient
                "gamma": [
                    "scale",
                    "auto"
                ],

                # Polynomial degree
                "degree": [2, 3, 4, 5],

                # Independent term for poly/sigmoid
                "coef0": [0.0, 0.1, 0.5, 1.0],

                # Class imbalance
                "class_weight": [
                    None,
                    "balanced"
                ]
            }




            #######################  ENSEMBLE ALGORITHMS ###############################

            Random_Forest_Classifier_params = {

                # Number of trees in the forest
                "n_estimators": randint(200, 801),

                # Maximum depth of each tree
                "max_depth": [
                    None,
                    5,
                    10,
                    15,
                    20,
                    30
                ],

                # Minimum samples required to split a node
                "min_samples_split": randint(2, 21),

                # Minimum samples required in a leaf
                "min_samples_leaf": randint(1, 11),

                # Split criterion
                "criterion": [
                    "gini",
                    "entropy",
                    "log_loss"
                ],

                # Number of features considered at each split
                "max_features": [
                    "sqrt",
                    "log2",
                    None
                ],

                # Maximum number of leaf nodes
                "max_leaf_nodes": [
                    None,
                    10,
                    20,
                    40,
                    80
                ],

                # Handling class imbalance
                "class_weight": [
                    None,
                    "balanced",
                    "balanced_subsample"
                ],

                # Cost-complexity pruning
                "ccp_alpha": [
                    0.0,
                    0.00001,
                    0.0001,
                    0.001,
                    0.01
                ]
            }


            Gradient_Boosting_Classifier_params = {

              # Number of boosting stages
              "n_estimators": randint(100, 501),

              # Contribution of each tree
              "learning_rate": [
                  0.01,
                  0.03,
                  0.05,
                  0.1,
                  0.2
              ],

              # Fraction of samples used for each boosting stage
              "subsample": [
                  0.7,
                  0.8,
                  0.9,
                  1.0
              ],

              # Maximum depth of each weak learner
              "max_depth": [
                  1,
                  2,
                  3,
                  4,
                  5
              ],

              # Minimum samples required to split an internal node
              "min_samples_split": randint(2, 21),

              # Minimum samples required in a leaf
              "min_samples_leaf": randint(1, 11),

              # Number of features considered for the best split
              "max_features": [
                  None,
                  "sqrt",
                  "log2"
              ],

              # Maximum number of leaf nodes
              "max_leaf_nodes": [
                  None,
                  10,
                  20,
                  40,
                  80
              ],

              # Loss function
              "loss": [
                  "log_loss",
                  "exponential"
              ],

              # Cost-complexity pruning
              "ccp_alpha": [
                  0.0,
                  1e-5,
                  1e-4,
                  1e-3,
                  1e-2
              ]
          }


              
      # AdaBoost
            AdaBoost_Classifier_params = {

              # Number of boosting stages
              "n_estimators": randint(50, 501),

              # Weight applied to each weak learner
              "learning_rate": [
                  0.01,
                  0.03,
                  0.05,
                  0.1,
                  0.2,
                  0.5,
                  1.0
              ],

              # Parameters of the underlying DecisionTreeClassifier
              "estimator__max_depth": [
                  1,
                  2,
                  3,
                  4
              ],

              # Minimum samples required to split a node
              "estimator__min_samples_split": randint(2, 21),

              # Minimum samples required in a leaf
              "estimator__min_samples_leaf": randint(1, 11),

              # Maximum number of leaf nodes
              "estimator__max_leaf_nodes": [
                  None,
                  5,
                  10,
                  20,
                  40
              ]
          }


            Bagging_Classifier_params = [
          {
              "n_estimators": randint(50, 501),

              "max_samples": [
                  0.5,
                  0.7,
                  0.8,
                  0.9,
                  1.0
              ],

              "max_features": [
                  0.5,
                  0.7,
                  0.8,
                  0.9,
                  1.0
              ],

              "bootstrap": [True],
              "bootstrap_features": [False, True],
              "oob_score": [False, True],

              "estimator__max_depth": [
                  None,
                  5,
                  10,
                  15,
                  20
              ],

              "estimator__min_samples_split": randint(2, 21),
              "estimator__min_samples_leaf": randint(1, 11),

              "estimator__max_leaf_nodes": [
                  None,
                  10,
                  20,
                  40,
                  80
              ]
          },

          {
              "n_estimators": randint(50, 501),

              "max_samples": [
                  0.5,
                  0.7,
                  0.8,
                  0.9,
                  1.0
              ],

              "max_features": [
                  0.5,
                  0.7,
                  0.8,
                  0.9,
                  1.0
              ],

              "bootstrap": [False],
              "bootstrap_features": [False, True],
              "oob_score": [False],

              "estimator__max_depth": [
                  None,
                  5,
                  10,
                  15,
                  20
              ],

              "estimator__min_samples_split": randint(2, 21),
              "estimator__min_samples_leaf": randint(1, 11),

              "estimator__max_leaf_nodes": [
                  None,
                  10,
                  20,
                  40,
                  80
              ]
          }
      ]


               
#####################################  XGBoost Classifier  ##################################

            XGBoost_params = {

              # Number of boosting rounds / trees
              "n_estimators": randint(100, 801),

              # Step size of each boosting round
              "learning_rate": loguniform(0.01, 0.3),

              # Maximum depth of each tree
              "max_depth": randint(2, 11),

              # Minimum sum of instance weight needed in a child
              "min_child_weight": randint(1, 11),

              # Minimum loss reduction required for a split
              "gamma": [0, 0.01, 0.1, 0.3, 0.5, 1, 2, 5],

              # Fraction of training rows used for each tree
              "subsample": uniform(0.6, 0.4),

              # Fraction of features used for each tree
              "colsample_bytree": uniform(0.6, 0.4),

              # L1 regularization
              "reg_alpha": loguniform(1e-4, 10),

              # L2 regularization
              "reg_lambda": loguniform(1e-3, 100),

              # Class imbalance
              "scale_pos_weight": [1, 1.5, 2, 3]
          }



########################################## DECISION TREEE ##################################"




            Decision_Tree_params = {

                  "criterion": ["gini", "entropy", "log_loss"],

                  "splitter": ["best", "random"],

                  "max_depth": [None, 5, 10, 15, 20, 30],

                  "min_samples_split": [2, 5, 10, 15, 20],

                  "min_samples_leaf": [1, 2, 4, 6, 10],

                  "max_features": ["sqrt", "log2", None],

                  "max_leaf_nodes": [None, 10, 20, 40, 80],

                  "class_weight": [None, "balanced"],

                  "ccp_alpha": [0.0, 0.0001, 0.001, 0.01]
              }


########################################   LightGBM_Classifier    #######################
            

            # LightGBM
            LightGBM_Classifier_params = {

                # Number of boosting trees
                "n_estimators": randint(100, 801),

                # Boosting learning rate
                "learning_rate": [
                    0.01,
                    0.03,
                    0.05,
                    0.1,
                    0.2
                ],

                # Maximum number of leaves per tree
                "num_leaves": [
                    15,
                    31,
                    63,
                    127
                ],

                # Maximum depth of each tree
                "max_depth": [
                    -1,
                    3,
                    5,
                    7,
                    10
                ],

                # Minimum number of samples in a leaf
                "min_child_samples": randint(5, 51),

                # Minimum Hessian / instance weight in a child
                "min_child_weight": [
                    1e-3,
                    1e-2,
                    0.1,
                    1.0
                ],

                # Minimum loss reduction required for a split
                "min_split_gain": [
                    0.0,
                    0.01,
                    0.1,
                    0.5
                ],

                # Fraction of rows used for each tree
                "subsample": [
                    0.7,
                    0.8,
                    0.9,
                    1.0
                ],

                # Fraction of features used for each tree
                "colsample_bytree": [
                    0.7,
                    0.8,
                    0.9,
                    1.0
                ],

                # L1 regularization
                "reg_alpha": [
                    0.0,
                    0.01,
                    0.1,
                    1.0
                ],

                # L2 regularization
                "reg_lambda": [
                    0.0,
                    0.01,
                    0.1,
                    1.0,
                    10.0
                ]
            }




################################################# CatBoost_Classifier #############################""
                          

              # CatBoost
            CatBoost_Classifier_params = {

                  # Number of boosting iterations / trees
                  "iterations": randint(200, 1001),

                  # Learning rate
                  "learning_rate": [
                      0.01,
                      0.03,
                      0.05,
                      0.1,
                      0.2
                  ],

                  # Tree depth
                  "depth": randint(4, 11),

                  # L2 regularization
                  "l2_leaf_reg": [
                      1,
                      3,
                      5,
                      10,
                      20
                  ],

                  # Randomness used when selecting splits
                  "random_strength": [
                      0.0,
                      0.5,
                      1.0,
                      2.0,
                      5.0
                  ],

                  # Bayesian bootstrap strength
                  "bagging_temperature": [
                      0.0,
                      0.5,
                      1.0,
                      2.0,
                      5.0
                  ],

                  # Number of splits used to bin numerical features
                  "border_count": [
                      32,
                      64,
                      128,
                      254
                  ],

                  # Tree growing strategy
                  "grow_policy": [
                      "SymmetricTree",
                      "Depthwise",
                      "Lossguide"
                  ],

                  # Automatic class weighting
                  "auto_class_weights": [
                      None,
                      "Balanced",
                      "SqrtBalanced"
                  ]
              }



####################################### NAIVE BASE #########################################

            Gaussian_NB_params = {
                                "var_smoothing": [
                                    1e-12,
                                    1e-11,
                                    1e-10,
                                    1e-9,
                                    1e-8,
                                    1e-7,
                                    1e-6,
                                    1e-5,
                                    1e-4,
                                    1e-3,
                                    1e-2,
                                    1e-1,
                                    1.0
                                ]
                            }


            return {
                  "logistic_regression": logistic_regression_par,
                  "lda": Linear_Discriminant_Analysis,
                  "qda": Quadratic_Discriminant_Analysis,
                  "knn": KNN_params,
                  "svm": SVM_params,
                  "random_forest": Random_Forest_Classifier_params,
                  "gradient_boosting": Gradient_Boosting_Classifier_params,
                  "adaboost": AdaBoost_Classifier_params,
                  "bagging": Bagging_Classifier_params,
                  "xgboost": XGBoost_params,
                  "decision_tree": Decision_Tree_params,
                  "lightgbm": LightGBM_Classifier_params,
                  "catboost": CatBoost_Classifier_params,
                  "gaussian_nb": Gaussian_NB_params
              }



    

                


            





            

                
                
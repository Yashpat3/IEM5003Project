import numpy as np
import csv,os
from sklearn.linear_model import LogisticRegression


class LogisticRegressor:

    # DO NOT EDIT
    def __init__(self, name,alpha,trainfilename,testfilename):
        self.name = name
        self.X, self.y = self.readData(trainfilename)
        self.X_test, self.y_test = self.readData(testfilename)
        self.alpha = alpha

        self.k = self.X.shape[1]
        self.n = self.X.shape[0]

        self.p = self.k+1

        self.reportfile = open(os.path.join("results","reports","LogisticRegressionReport_{}.txt".format(self.name)), "w")
        self.reportfile.write("RESULT FOR LOGISTIC REGRESSION ON {} data\n".format(self.name))
        self.reportfile.write("Training Data File : {}\n".format(trainfilename))
        self.reportfile.write("Test Data File : {}\n".format(testfilename))
        self.reportfile.write("The no of variables : {}, no of entries : {}, no of regression coefficients : {}\n".format(self.k, self.n, self.p))

    # DO NOT EDIT
    def readData(self,filename):
        #DO NOT EDIT
        X = []
        y = []

        # Load data set
        with open(filename) as f:
            next(f, None)
            for line in csv.reader(f, delimiter=","):
                X.append(line[:-1])
                y.append(line[-1])

        X = np.array(X, dtype=float)
        y = np.array(y, dtype=int)

        return X,y

    # DO NOT EDIT BUT READ THIS FUNCTION VERY CAREFULLY!
    # THIS FUNCTION LAYS OUT THE OVERALL WORKFLOW
    def evaluateRegressor(self):

        #The linear regression function outputs a linear regression object, the R2 score,
        #the regression parameters and the predicted values based on X and y values that have been read.
        log_reg, log_score, log_params, log_y_pred = self.logisticRegression(self.X,self.y)

        #This function must take in the predicted values and output the residuals based on the existing y values
        log_residuals = self.computeResiduals(log_y_pred,self.y)

        self.reportfile.write("R^2 score : {}\n".format(log_score))
        self.reportfile.write("Regression parameters : {}\n".format(log_params))

        self.reportfile.close()

        print("\n\n\n\n")

        y_test_pred = self.predictNewObservations(log_reg,self.X_test)

        return y_test_pred-self.y_test

    def logisticRegression(self, X, y):
        #TODO: do logistic regression

        #TODO: obtain coefficient of determination

        #TODO: obtain prediction parameters

        #TODO: do prediction on data

        return reg, score, params, y_pred

    def computeResiduals(self, y_pred, y):
        #TODO: compute residuals

        return residuals

    def predictNewObservations(self, lin_reg, X):
        #TODO: predict on new data

        return y_test_pred

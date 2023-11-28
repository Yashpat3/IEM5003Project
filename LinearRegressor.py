import numpy as np
import csv, os
from sklearn.linear_model import LinearRegression
import scipy.stats as stats

class LinearRegressor:

    # DO NOT EDIT
    def __init__(self, name,alpha,trainfilename,testfilename):
        self.name = name
        self.X, self.y = self.readData(trainfilename)
        self.X_test, self.y_test = self.readData(testfilename)
        self.alpha = alpha

        self.k = self.X.shape[1]
        self.n = self.X.shape[0]

        self.p = self.k+1

        self.reportfile = open(os.path.join("results","reports","LinearRegressionReport_{}.txt".format(self.name)), "w")
        self.reportfile.write("RESULT FOR LINEAR REGRESSION ON {} data\n".format(self.name))
        self.reportfile.write("Training Data File : {}\n".format(trainfilename))
        self.reportfile.write("Test Data File : {}\n".format(testfilename))
        self.reportfile.write("The no of variables : {}, no of entries : {}, no of regression coefficients : {}\n".format(self.k, self.n, self.p))

    # DO NOT EDIT
    @staticmethod
    def readData(filename):
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
        y = np.array(y, dtype=float)

        return X,y

    # DO NOT EDIT
    def hypothesisTestFScoreMethod(self, f, f_0):
        if f_0 > f:
            print("reject null hypothesis: output COULD BE LINEARLY related to one or more input features")
            return True
        else:
            print(
                "fail to reject null hypothesis: output MAY NOT BE LINEARLY related to one or more input features")
            return False

    # DO NOT EDIT
    def hypothesisTestPValue(self, pValue):
        # DO NOT EDIT
        if pValue < self.alpha:
            print("reject null hypothesis: output COULD BE LINEARLY related to one or more input features")
            return True
        else:
            print(
                "fail to reject null hypothesis: output MAY NOT BE LINEARLY related to one or more input features")
            return False

    # DO NOT EDIT BUT READ THIS FUNCTION VERY CAREFULLY!
    # THIS FUNCTION LAYS OUT THE OVERALL WORKFLOW
    def evaluateRegressor(self):

        #The linear regression function outputs a linear regression object, the R2 score,
        #the regression parameters and the predicted values based on X and y values that have been read.
        lin_reg, lin_score, lin_params, lin_y_pred = self.linearRegression(self.X,self.y)

        #This function must take in the predicted values and output the residuals based on the existing y values
        lin_residuals = self.computeResiduals(lin_y_pred,self.y)

        self.reportfile.write("R^2 score : {}\n".format(lin_score))
        self.reportfile.write("Regression parameters : {}\n".format(lin_params))

        #This function computes the F score based on alpha, k, n, p
        f = self.computeFScore(self.alpha,self.k,self.n,self.p)
        self.reportfile.write("F Score : {}\n".format(f))

        #This function computes the F statistic based on lin_y_pred, alpha, k, n, p
        f_0 = self.computeFTestStatistic(lin_y_pred,self.y,lin_residuals,self.alpha,self.k,self.n,self.p)

        self.reportfile.write("Test Statistic : {}\n".format(f_0))

        #This function computes the F score based on test statistic, alpha, k, n, p
        pValue = self.computepValue(f_0,self.alpha,self.k,self.n,self.p)

        self.reportfile.write("P-Value : {}\n".format(pValue))

        #This check has been provided for you to be able to verify whether your answer makes sense
        if self.hypothesisTestFScoreMethod(f, f_0) != self.hypothesisTestPValue(pValue):
            self.reportfile.write("Your Testing definitely has an error\n")

        else:
            self.reportfile.write("Both tests returned the same result\n")

        #print("\n\n\n\n")

        y_test_pred = self.predictNewObservations(lin_reg,self.X_test)

        return y_test_pred-self.y_test

    def linearRegression(self, X, y):
        #TODO: do linear regression

        #TODO: obtain coefficient of determination

        #TODO: obtain prediction parameters

        #TODO: do prediction on data

        return reg, score, params, y_pred

    def computeResiduals(self,y_pred,y):
        #TODO: compute residuals

        return residuals

    def computeSSE(self,residuals):

        #TODO: compute SSE

        return SSE

    def computeSSR(self,y_pred,y):

        #TODO: compute SSR

        return SSR

    def computeFScore(self,alpha,k,n,p):

        #TODO: compute Fscore

        return f

    def computeFTestStatistic(self,y_pred,y,residuals,alpha,k,n,p):

        #TODO: compute test statistic

        #TODO: test statistic
        return f_0

    def computepValue(self,test_statistic,alpha,k,n,p):

        #TODO: compute p-value

        return pValue

    def predictNewObservations(self,lin_reg,X):

        #TODO: predict new data

        return y_test_pred



import matplotlib.pyplot as plt
import os

def liverDataPredictionErrorHistogram(lin1_y_test_pred_err):
    #TODO: plot histogram
    plt.savefig(os.path.join("results","plots","LiverTestLinearRegressionError.pdf"))
    plt.clf()

def linearAndLogisticRegressionErrorComparison(lin_y_test_pred_err,log_y_test_pred_err):
    #TODO: plot histogram
    plt.savefig(os.path.join("results","plots","WineQualityLinearRegressionError.pdf"))
    plt.clf()

    #TODO: plot histogram
    plt.savefig(os.path.join("results","plots","WineQualityLogisticRegressionError.pdf"))
    plt.clf()

def visualizeGammaGlutamylHalfPintsScatterPlot(X,path):
    gammaGlutamylData = X[:,3]
    halfPintsData = X[:,4]
    #TODO: plot scatterplot
    plt.savefig(path)
    plt.clf()

def visualizeAlanineATBoxPlot(X,path):
    alanineATData = X[:, 2]

    #TODO: plot boxplot
    plt.savefig(path)
    plt.clf()

def visualizeMCVHistogram(X,path):
    MCVData = X[:, 0]

    #TODO: plot histogram

    plt.savefig(path)
    plt.clf()

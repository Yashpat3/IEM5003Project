import matplotlib.pyplot as plt
import os

def liverDataPredictionErrorHistogram(lin1_y_test_pred_err):
    #TODO: plot histogram
    plt.hist(lin1_y_test_pred_err, bins = "auto" , edgecolor = "red")
    plt.savefig(os.path.join("results","plots","LiverTestLinearRegressionError.pdf"))
    plt.clf()

def linearAndLogisticRegressionErrorComparison(lin_y_test_pred_err,log_y_test_pred_err):
    #TODO: plot histogram
    plt.hist(lin_y_test_pred_err, bins = "auto" , edgecolor = "black")
    plt.savefig(os.path.join("results","plots","WineQualityLinearRegressionError.pdf"))
    plt.clf()

    #TODO: plot histogram
    plt.hist(log_y_test_pred_err, bins = "auto" , edgecolor = "black")
    plt.savefig(os.path.join("results","plots","WineQualityLogisticRegressionError.pdf"))
    plt.clf()

def visualizeGammaGlutamylHalfPintsScatterPlot(X,path):
    gammaGlutamylData = X[:,3]
    halfPintsData = X[:,4]
    plt.scatter(gammaGlutamylData, halfPintsData)
    plt.xlabel("gammaGlutamy")
    plt.ylabel("HalfPints")
    #TODO: plot scatterplot
    plt.savefig(path)
    plt.clf()

def visualizeAlanineATBoxPlot(X,path):
    alanineATData = X[:, 2]

    #TODO: plot boxplot
    plt.boxplot(alanineATData)
    plt.savefig(path)
    plt.clf()

def visualizeMCVHistogram(X,path):
    MCVData = X[:, 0]

    #TODO: plot histogram
    plt.hist(MCVData, bins = "auto", edgecolor = "black")

    plt.savefig(path)
    plt.clf()

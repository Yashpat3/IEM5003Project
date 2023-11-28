import numpy as np
from scipy.stats import t,chi2

def HypothesisTest1():
    data = [261.3, 259.4, 265.7, 270.6, 274.2, 261.4, 254.5, 283.7,
            258.1, 270.5, 255.1, 268.9, 267.4, 253.6, 234.3, 263.2,
            254.2, 270.7, 233.7, 263.5, 244.5, 251.8, 259.5, 257.5,
            257.7, 272.6, 253.7, 262.2, 252.0, 280.3, 274.9, 233.7,
            237.9, 274.0, 264.5, 244.8, 264.0, 268.3, 272.1, 260.2,
            255.8, 260.7, 245.5, 279.6, 237.8, 278.5, 273.3, 263.7,
            241.4, 260.6, 280.3, 272.7, 261.0, 260.0, 279.3, 252.1,
            244.3, 272.2, 248.3, 278.7, 236.0, 271.2, 279.8, 245.6,
            241.2, 251.1, 267.0, 273.4, 247.7, 254.8, 272.8, 270.5,
            254.4, 232.1, 271.5, 242.9, 273.6, 256.1, 251.6,
            256.8, 273.0, 240.8, 276.6, 264.5, 264.5, 226.8,
            255.3, 266.6, 250.2, 255.8, 285.3, 255.4, 240.5,
            255.0, 273.2, 251.4, 276.1, 277.8, 266.8, 268.5
            ]
    reportfile = open("results/reports/HypothesisTestQuestion1.txt", "w")
    reportfile.write("Question 1.A: Construct Hypothesis Test that mean distance exceeds 280 yards\n"+
          "\t H_0: mu=280 \n"+
          "\t H_1: mu>280 \n"+
          "\t alpha=0.05 \n")

    alpha = 0.05

    # TODO: find out the number of observations (NO HARDCODING ALLOWED, determine using built in python or numpy functions for eg: len(data))
    n = 0

    # TODO:start out with assuming null hypothesis is true
    mu = 0

    # TODO:calculate sample mean
    x_bar = 0

    # TODO:calculate sample variance
    s = 0

    # TODO:test statistic (using t-distribution)
    t_0 = 0

    # TODO:determine degrees of freedom
    df = 0

    # TODO:calculate t(alpha,n-1) critical region
    t_alpha_n_1 = 0

    reportfile.write("\t x_bar:{} \t s:{} \t t_0:{} \t df:{} \t t_alpha_n_1:{}\n".format(x_bar, s, t_0, df, t_alpha_n_1))

    if t_0 > t_alpha_n_1:
        reportfile.write("\t Reject H_0: There is sufficient evidence that mean distance is greater than 280\n")
    else:
        reportfile.write("\t Fail to Reject H_0: There is INSUFFICIENT evidence that mean distance is greater than 280\n")

    reportfile.close()

def HypothesisTest2():
    data = [3.481, 3.448, 3.485, 3.475, 3.472,
            3.477, 3.472, 3.464, 3.472, 3.470,
            3.470, 3.470, 3.477, 3.473, 3.474
            ]

    reportfile = open("results/reports/HypothesisTestQuestion2.txt", "w")
    reportfile.write("HypothesisTestQuestion 2.A: Construct Hypothesis Test that measurement standard deviation differ from 0.01 grams?\n"+
          "\t H_0: sigma^2=0.01^2 \n"+
          "\t H_1: sigma^2 != 0.01^2 \n"+
          "\t alpha=0.05 \n")

    alpha = 0.05

    # TODO: find out the number of observations (NO HARDCODING ALLOWED, determine using built in python or numpy functions for eg: len(data))
    n = 0

    # TODO:start out with assuming null hypothesis is true
    sigma2 = 0

    # TODO:determine degrees of freedom df
    df = 0

    # TODO:compute sample variance
    s2 = 0

    # TODO:compute test statistic
    chi2_0 = 0

    # TODO:compute chi2_1_alpha_n_1,chi2alpha_n_1 ie. limits of critical region
    chi2_1_alpha_n_1 = 0
    chi2_alpha_n_1 = 0

    reportfile.write("\t s2:{} \t df:{} \t ch2_0:{} \t chi2_1_alpha_n_1:{} \t chi2_alpha_n_1:{}\n".format(s2, df, chi2_0,
                                                                                               chi2_1_alpha_n_1,
                                                                                               chi2_alpha_n_1))

    if chi2_0 < chi2_alpha_n_1 or chi2_0 > chi2_1_alpha_n_1:
        reportfile.write(
            "\t Reject H_0: There is sufficient evidence that measurement standard deviation differ from 0.01 grams\n")
    else:
        reportfile.write(
            "\t Fail to Reject H_0: There is INSUFFICIENT evidence that measurement standard deviation differ from 0.01 grams\n")

    reportfile.write(
        "HypothesisTestQuestion 2.B: Obtain P-Value for Hypothesis Test that measurement standard deviation differ from 0.01 grams?\n"+
        "\t H_0: sigma^2=0.01^2 \n"+
        "\t H_1: sigma^2 != 0.01^2 \n"+
        "\t alpha=0.05 \n")

    #TODO: Calculate pvalue
    pvalue = 0

    reportfile.write("\t pval:{}\n".format(pvalue))

    reportfile.close()

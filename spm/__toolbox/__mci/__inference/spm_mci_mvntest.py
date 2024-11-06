from spm.__wrapper__ import Runtime


def spm_mci_mvntest(*args, **kwargs):
    """
      Test for multivariate normality  
        FORMAT [stats] = spm_mci_mvntest (X,df)  
         
        X         [N x d] data matrix containing N IID samples of d-variate data  
        df        Degrees of freedom e.g. df <= N  
         
        stats  
        .p        p-value for multivariate normality  
                  e.g. with p < 0.05 one can reject null hypothesis of normality   
        .W(j)     Shapiro-Wilks statistic for jth variate  
        .Z(j)     Equivalent standardised Gaussian variate for W(j)  
        .pusw(j)  p-value for normality of jth variate (Shapiro-Wilks)  
        .puks(k)  p-value for normality of jth variate (Kolmogorov-Smirnoff)  
        .k        kurtosis of jth variate  
        .s        skewness of jth variate  
         
        This function is adapted from the matlab function Roystest.m:  
         
        Trujillo-Ortiz, A., R. Hernandez-Walls, K. Barba-Rojo and  
          L. Cupul-Magana. (2007). Roystest:Royston's Multivariate Normality Test.     
          A MATLAB file. [WWW document]. URL http://www.mathworks.com/  
          matlabcentral/fileexchange/loadFile.do?objectId=17811  
         
        Royston, J.P. (1992). Approximating the Shapiro-Wilk W-Test for non-  
             normality. Statistics and Computing, 2:117-119.  
             121-133.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_mvntest.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_mvntest", *args, **kwargs)

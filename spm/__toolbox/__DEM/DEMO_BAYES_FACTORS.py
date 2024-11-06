from spm.__wrapper__ import Runtime


def DEMO_BAYES_FACTORS(*args, **kwargs):
    """
      FORMAT DEMO_BAYES_FACTORS(pC,hE,hC,N)  
        Demonstration Bayes factors and classical p-values  
       --------------------------------------------------------------------------  
        pC   - prior covariance             (e.g., 4)  
        hE   - expectation of log precision (e.g., 1)  
        hC   - covariance of log precision  (e.g., 1/8)  
        N    - number of observations       (e.g., 16)  
        b    - relative variance under alternate and null (e.g., 1/32)  
         
        This demonstration routine uses a simple linear model to examine the  
        relationship between free energy differences or log Bayes factors and  
        classical F statistics. Using re-randomisation of a design matrix, it  
        computes the null distribution over both statistics and plots them  
        against each other.  There is a linear relationship, which allows one to  
        evaluate the false-positive rate for any threshold on the Bayes factor.  
        Ideally, one would like to see a positive log Bayes factor map to a  
        classical threshold of p=0.05. The offset and slope of the linear  
        relationship between the two statistics depends upon prior beliefs about  
        the covariance of the parameters and the log precision. These can be  
        changed by editing the code below (or supplying input arguments).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_BAYES_FACTORS.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_BAYES_FACTORS", *args, **kwargs, nargout=0)

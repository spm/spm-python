from spm.__wrapper__ import Runtime


def DEMO_Lindley_paradox(*args, **kwargs):
    """
      FORMAT DEMO_BAYES_FACTORS(pC,hE,hC)  
        Demonstration Bayes factors and classical p-values  
       --------------------------------------------------------------------------  
        pC   - prior covariance             (e.g., 4)  
        hE   - expectation of log precision (e.g., 1)  
        hC   - covariance of log precision  (e.g., 1/8)  
         
        This demonstration routine uses a simple linear model to examine the  
        relationship between free energy differences or log Bayes factors and  
        classical F statistics.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_Lindley_paradox.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_Lindley_paradox", *args, **kwargs, nargout=0)

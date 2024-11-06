from spm.__wrapper__ import Runtime


def spm_GPclass(*args, **kwargs):
    """
      Gaussian process classification  
        [p,F,K,theta,bic] = spm_GPclass(XX,t,lab,cov_fun,fun_args)  
        Inputs:  
            XX       - cell array of dot product matrices  
                       for training and testing data  
            t        - target values for training data  
            lab      - binary array indicating which are training data  
            cov_fun  - function for building covariance matrix  
            fun_args - additional arguments for covariance function  
        Outputs  
            p     - Belonging probabilities  
            F     - Log-likelihood  
            K     - Covariance matrix  
            bic   - Adjustment to log-likelihood to account for hyper-parameter estimation  
         
        See Chapter 3 of:  
        C. E. Rasmussen & C. K. I. Williams, Gaussian Processes for Machine Learning, the MIT Press, 2006,  
        ISBN 026218253X. c 2006 Massachusetts Institute of Technology. www.GaussianProcess.org/gpml  
        or Bishop (2006) "Pattern Recognition and Machine Learning"  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_GPclass.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_GPclass", *args, **kwargs)

from spm.__wrapper__ import Runtime


def DEMO_SLR(*args, **kwargs):
    """
      Demo of sparse logistic regression. This demonstration routines  
        illustrates the use of sparse acoustic regression (as implemented in   
        spm_sparse_regression.m) to recover a small number of causes that best  
        explain some dependent variable. For example, imagine we thought that a  
        small number (e.g., four) of SNPs or copy number variants a generic study  
        had sufficiently large effect sizes on some phenotypic measure to be  
        worth pursuing. We might treat these (rare variants) as being expressed  
        in the context of random effects (e.g., common variants and phenotypic  
        measurement noise); however, we have many more potential causes than  
        observations. This problem is addressed using (logistic) regression  
        under sparsity constraints specified in terms of hyper priors over the  
        precision (i.e. inverse variance) of model parameters. This provides the  
        Bayesian shrinkage estimators of the regression coefficients that,  
        crucially, can then be subject to Bayesian model reduction. Bayesian  
        model reduction effectively eliminates redundant parameters that provided  
        the optimal balance between accuracy and complexity.  
         
        in the example below, we assume that we have 32 subjects with 128   
        independent variables (e.g., following some initial dimension reduction).  
        The simulated data is generated with just four of the independent to see   
        whether these can be identified using sparse logistic regression and  
        Bayesian model reduction.  
         
        If the dependent variables are classes or probabilities a logistic  
        transform is automatically applied. However, one can also use this  
        routine for continuous (i.e., parametric phenotypes). the graphics  
        produced by this demo report the results of sparse logistic regression  
        using variational Laplace (i.e., approximate Bayesian inference and hyper  
        priors). In addition, it reports the results and summary of the  
        subsequent Bayesian model reduction.  
         
        see also: spm_sparse_regression.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_SLR.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_SLR", *args, **kwargs, nargout=0)

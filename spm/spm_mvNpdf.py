from spm.__wrapper__ import Runtime


def spm_mvNpdf(*args, **kwargs):
    """
      Probability Density Function (PDF) of multivariate Normal distribution  
        FORMAT pdf = spm_Npdf(z,Mu,V)  
         
        z  - ordinates  
        Mu - mean (a d-vector)  
        V  - d x d variance-covariance matrix  
       __________________________________________________________________________  
         
        spm_Npdf returns the Probability Density Function (PDF) for the  
        multivariate Normal (Gaussian) family of distributions.  
         
        The dimension of the Normal distribution is taken as the length of Mu.  
        V must be a d x d variance-covariance matrix.  
         
        For the univariate Normal distribution (d=1), z can be a matrix of  
        arbitrary dimensions - each entry is treated separately and the PDF  
        returned as the corresponding element in a matrix of the same size.  
         
        For multivarate PDFs, the ordinates must be in the columns of z, so  
        z must have column dimension d. Multiple columns can be entered.   
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mvNpdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mvNpdf", *args, **kwargs)

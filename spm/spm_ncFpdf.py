from spm.__wrapper__ import Runtime


def spm_ncFpdf(*args, **kwargs):
    """
      Probability Density Function (PDF) of non-central F-distribution  
        FORMAT f = spm_ncFpdf(x,df,d)  
        x  - F-variate (F has range [0,Inf) )  
        df - degrees of freedom, df = [v,w] with v>0 and w>0  
        d  - non-centrality parameter  
        f  - PDF of non-central F-distribution with [v,w] degrees of freedom (df)  
             and non-centrality parameter d at points x  
       __________________________________________________________________________  
         
        spm_ncFpdf implements the Probability Density Function of non-central   
        F-distributions.  
         
        References:  
        https://en.wikipedia.org/wiki/Noncentral_F-distribution  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ncFpdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ncFpdf", *args, **kwargs)

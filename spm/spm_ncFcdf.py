from spm._runtime import Runtime


def spm_ncFcdf(*args, **kwargs):
    r"""
      Cumulative Distribution Function (CDF) of non-central F-distribution  
        FORMAT f = spm_ncFcdf(x,df,d)  
        x  - F-variate (F has range [0,Inf) )  
        df - degrees of freedom, df = [v,w] with v>0 and w>0  
        d  - non-centrality parameter  
        F  - CDF of non-central F-distribution with [v,w] d.f. at points x  
         
        Reference:  
        https://en.wikipedia.org/wiki/Noncentral_F-distribution  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ncFcdf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ncFcdf", *args, **kwargs)

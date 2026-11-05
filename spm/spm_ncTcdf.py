from spm._runtime import Runtime


def spm_ncTcdf(*args, **kwargs):
    r"""
      Cumulative Distribution Function (CDF) of non-central t-distribution  
        FORMAT F = spm_ncTcdf(x,v,d)  
        x - T-variate (Student's t has range (-Inf,Inf))  
        v - degrees of freedom (v>0, non-integer d.f. accepted)  
        d - non-centrality parameter  
        F - CDF of non-central t-distribution with v d.f. at points x  
         
        Reference:  
       --------------------------------------------------------------------------  
        Algorithm AS 243: Cumulative Distribution Function of the Non-Central t  
        Distribution  
        Russell V. Lenth  
        Applied Statistics, Vol. 38, No. 1 (1989), pp. 185-189  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ncTcdf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ncTcdf", *args, **kwargs)

from spm._runtime import Runtime


def spm_ncTpdf(*args, **kwargs):
    r"""
      Probability Density Function (PDF) of non-central t-distribution  
        FORMAT f = spm_ncTpdf(x,v,d)  
        x - t-ordinates  
        v - degrees of freedom (v>0, non-integer d.f. accepted)  
        d - non-centrality parameter  
        f - PDF of non-central t-distribution with v degrees of freedom (df) and  
            non-centrality parameter d at points x  
       __________________________________________________________________________  
         
        spm_ncTpdf implements the Probability Density Function of non-central   
        t-distributions.  
         
        References:  
        https://en.wikipedia.org/wiki/Noncentral_t-distribution  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ncTpdf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ncTpdf", *args, **kwargs)

from spm.__wrapper__ import Runtime


def spm_ncTpdf(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ncTpdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ncTpdf", *args, **kwargs)

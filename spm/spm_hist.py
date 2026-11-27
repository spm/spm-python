from spm._runtime import Runtime


def spm_hist(*args, **kwargs):
    r"""
      Generate a weighted histogram - a compiled routine  
        FORMAT h = spm_hist(ind,val)  
        ind - indices (unsigned byte)  
        val - weights  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_hist.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_hist", *args, **kwargs)

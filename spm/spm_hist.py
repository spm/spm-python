from spm.__wrapper__ import Runtime


def spm_hist(*args, **kwargs):
    """
      Generate a weighted histogram - a compiled routine  
        FORMAT h = spm_hist(ind,val)  
        ind - indices (unsigned byte)  
        val - weights  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_hist.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_hist", *args, **kwargs)

from spm._runtime import Runtime


def spm_uncat(*args, **kwargs):
    r"""
      Convert a matrix into an array  
        FORMAT [a] = spm_uncat(x,a)  
        x - matrix  
        a - cell array  
         
        i.e. a = spm_uncat(spm_cat(a),a)  
         
        see also spm_vec and spm_unvec  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_uncat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_uncat", *args, **kwargs)

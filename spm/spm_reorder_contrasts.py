from spm._runtime import Runtime


def spm_reorder_contrasts(*args, **kwargs):
    r"""
      Recompute contrasts allowing for permutation and deletion  
        FORMAT batch = spm_reorder_contrasts(SPM,order)  
        SPM   - SPM data structure  
        order - array of contrast indices  
         
        batch - batch job  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_reorder_contrasts.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_reorder_contrasts", *args, **kwargs)

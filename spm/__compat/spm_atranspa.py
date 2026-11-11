from spm._runtime import Runtime


def spm_atranspa(*args, **kwargs):
    r"""
      Multiplies the transpose of a matrix by itself  
        FORMAT C = spm_atranspa(A)  
        A - real matrix  
        C - real symmetric matrix resulting from A'A  
       _______________________________________________________________________  
         
        This compiled routine was written to save both memory and CPU time but  
        is now deprecated. Use A'*A directly instead.  
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/compat/spm_atranspa.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_atranspa", *args, **kwargs)

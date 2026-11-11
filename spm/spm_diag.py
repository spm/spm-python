from spm._runtime import Runtime


def spm_diag(*args, **kwargs):
    r"""
      Diagonal matrices and diagonals of a matrix  
         
        SPM_DIAG generalises the function "diag" to also work with cell arrays.  
        See DIAG's help for syntax.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_diag.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_diag", *args, **kwargs)

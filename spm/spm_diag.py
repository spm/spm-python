from spm.__wrapper__ import Runtime


def spm_diag(*args, **kwargs):
    """
      Diagonal matrices and diagonals of a matrix  
         
        SPM_DIAG generalises the function "diag" to also work with cell arrays.  
        See DIAG's help for syntax.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_diag.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_diag", *args, **kwargs)

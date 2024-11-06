from spm.__wrapper__ import Runtime


def spm_atranspa(*args, **kwargs):
    """
      Multiplies the transpose of a matrix by itself  
        FORMAT C = spm_atranspa(A)  
        A - real matrix  
        C - real symmetric matrix resulting from A'A  
       _______________________________________________________________________  
         
        This compiled routine was written to save both memory and CPU time but  
        is now deprecated. Use A'*A directly instead.  
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_atranspa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_atranspa", *args, **kwargs)

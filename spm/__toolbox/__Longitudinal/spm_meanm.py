from spm.__wrapper__ import Runtime


def spm_meanm(*args, **kwargs):
    """
      Compute barycentre of matrix exponentials  
        FORMAT M = spm_meanm(A)  
        A - A 3D array, where each slice is a matrix  
        M - the resulting mean  
         
        Note that matrices should not be too dissimilar to each other or the  
        procedure fails.  
        See http://hal.archives-ouvertes.fr/hal-00699361/  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Longitudinal/spm_meanm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_meanm", *args, **kwargs)

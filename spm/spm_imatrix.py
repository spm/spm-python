from spm._runtime import Runtime


def spm_imatrix(*args, **kwargs):
    r"""
      Return the parameters for creating an affine transformation matrix  
        FORMAT P = spm_imatrix(M)  
        M   - Affine transformation matrix  
        P   - Parameters (see spm_matrix for definitions)  
       __________________________________________________________________________  
         
        See also: spm_matrix.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_imatrix.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_imatrix", *args, **kwargs)

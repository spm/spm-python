from spm._runtime import Runtime


def spm_large_dcm_reduce(*args, **kwargs):
    r"""
      Optimise the number of prior connectivity eigenmodes  
        FORMAT [DCM,S] = spm_large_dcm_reduce(DCM)  
        DCM    - DCM structure  
        S      - log-evidences  
         
        This routine optimises the number of eigenmodes of the prior covariance  
        matrix using the eigenvectors of the functional connectivity matrix. The  
        optimisation uses post hoc model reduction.  
       __________________________________________________________________________  
         
        Reference  
         
        M.L. Seghier and K.J. Friston, "Network discovery with large DCMs".  
        NeuroImage, 68:181-191, 2013.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_large_dcm_reduce.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_large_dcm_reduce", *args, **kwargs)

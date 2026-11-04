from spm._runtime import Runtime


def spm_DEM_qH(*args, **kwargs):
    r"""
      Report on conditional estimates of hyperparameters  
        FORMAT spm_DEM_qH(qH,pH)  
         
        qH.h    - conditional estimate of log-precision (causes)  
        qH.g    - conditional of log-precision (state)  
        qH.V    - conditional variance (causes)  
        qH.W    - conditional (states)  
         
        qH.p    - time-dependent estimates from Laplace scheme  
        qH.c    - time-dependent covariances  
         
        pH      - option true log-precisions  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_DEM_qH.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_qH", *args, **kwargs, nargout=0)

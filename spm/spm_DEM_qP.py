from spm._runtime import Runtime


def spm_DEM_qP(*args, **kwargs):
    r"""
      Report on conditional estimates of parameters  
        FORMAT spm_DEM_qP(qP,pP)  
         
        qP.P   - conditional expectations  
        qP.V   - conditional variance  
         
        pP     - optional priors  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_DEM_qP.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_qP", *args, **kwargs, nargout=0)

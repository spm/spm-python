from spm._runtime import Runtime


def spm_write_residuals(*args, **kwargs):
    r"""
      Write residual images  
        FORMAT Vres = spm_write_residuals(SPM,Ic)  
        SPM    - structure containing generic analysis details  
        Ic     - contrast index used to adjust data (0:   no adjustment)  
                                                    (NaN: adjust for everything)   
         
        VRes   - struct array of residual image handles  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_write_residuals.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_write_residuals", *args, **kwargs)

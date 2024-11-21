from spm.__wrapper__ import Runtime


def spm_write_residuals(*args, **kwargs):
    """
      Write residual images  
        FORMAT Vres = spm_write_residuals(SPM,Ic)  
        SPM    - structure containing generic analysis details  
        Ic     - contrast index used to adjust data (0:   no adjustment)  
                                                    (NaN: adjust for everything)   
         
        VRes   - struct array of residual image handles  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_write_residuals.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_write_residuals", *args, **kwargs)

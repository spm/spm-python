from spm.__wrapper__ import Runtime


def spm_hdm_ui(*args, **kwargs):
    """
      User interface for hemodynamic model estimation  
        FORMAT [Ep,Cp,K1,K2] = spm_hdm_ui(xSPM,SPM,hReg  
         
        xSPM   - structure containing specific SPM details  
        SPM    - structure containing generic  SPM details  
        hReg   - Handle of results section XYZ registry (see spm_results_ui.m)  
         
        Ep     - conditional expectations of the hemodynamic model parameters  
        Cp     - conditional  covariance  of the hemodynamic model parameters  
        K1     - 1st order kernels  
        K2     - 2nd order kernels  
                 (see main body of routine for details of model specification)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_hdm_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_hdm_ui", *args, **kwargs)

from spm.__wrapper__ import Runtime


def spm_dcm_bma_results(*args, **kwargs):
    """
      Plot histograms from BMA for selected modulatory and driving input  
        FORMAT spm_dcm_bma_results(BMS,method)  
        BMS        - BMS.mat file  
        method     - inference method (FFX or RFX)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_bma_results.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_bma_results", *args, **kwargs, nargout=0)

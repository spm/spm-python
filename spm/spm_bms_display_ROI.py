from spm._runtime import Runtime


def spm_bms_display_ROI(*args, **kwargs):
    r"""
      Display results from BMS in a region of interest (ROI)  
        FORMAT spm_bms_display_ROI (BMS,mask,method)  
         
        Input:  
        BMS    - BMS.mat file   
        mask   - region of interest image  
        method - inference method (FFX or RFX)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_bms_display_ROI.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bms_display_ROI", *args, **kwargs, nargout=0)

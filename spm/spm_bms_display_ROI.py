from mpython import Runtime


def spm_bms_display_ROI(*args, **kwargs):
    """
      Display results from BMS in a region of interest (ROI)
        FORMAT spm_bms_display_ROI (BMS,mask,method)

        Input:
        BMS    - BMS.mat file
        mask   - region of interest image
        method - inference method (FFX or RFX)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bms_display_ROI.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bms_display_ROI", *args, **kwargs, nargout=0)

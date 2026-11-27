from spm._runtime import Runtime


def spm_bms_display(*args, **kwargs):
    r"""
      Display results from BMS Maps  
        FORMAT spm_bms_display(BMS,action)  
         
        Input:  
        BMS    - BMS containing details of excursion set  
        action - 'Init' (Initialise)  
                 'do_plot' (plot voxel results)  
                 'save' (save results as NIfTI image)  
                 'overlays' (options overlays menu)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_bms_display.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bms_display", *args, **kwargs)

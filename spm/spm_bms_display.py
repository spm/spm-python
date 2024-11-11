from spm.__wrapper__ import Runtime


def spm_bms_display(*args, **kwargs):
    """
      Display results from BMS Maps  
        FORMAT spm_bms_display(BMS,action)  
         
        Input:  
        BMS    - BMS containing details of excursion set  
        action - 'Init' (Initialise)  
                 'do_plot' (plot voxel results)  
                 'save' (save results as NIfTI image)  
                 'overlays' (options overlays menu)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bms_display.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_bms_display", *args, **kwargs)

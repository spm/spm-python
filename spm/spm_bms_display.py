from spm.__wrapper__ import Runtime


def spm_bms_display(*args, **kwargs):
  """  Display results from BMS Maps  
    FORMAT spm_bms_display(BMS,action)  
     
    Input:  
    BMS    - BMS containing details of excursion set  
    action - 'Init' (Initialise)  
             'do_plot' (plot voxel results)  
             'save' (save results as NIfTI image)  
             'overlays' (options overlays menu)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_bms_display.m)
  """

  return Runtime.call("spm_bms_display", *args, **kwargs)

from spm.__wrap__ import _Runtime


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

  return _Runtime.call("spm_bms_display", *args, **kwargs)

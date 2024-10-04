from spm.__wrap__ import _Runtime


def spm_bms_display_ROI(*args, **kwargs):
  """  Display results from BMS in a region of interest (ROI)  
    FORMAT spm_bms_display_ROI (BMS,mask,method)  
     
    Input:  
    BMS    - BMS.mat file   
    mask   - region of interest image  
    method - inference method (FFX or RFX)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_bms_display_ROI.m)
  """

  return _Runtime.call("spm_bms_display_ROI", *args, **kwargs, nargout=0)

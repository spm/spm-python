from spm.__wrapper__ import Runtime


def spm_eeg_inv_image_display(*args, **kwargs):
  """  Display an interpolated 3D image or mesh of a contrast or window  
     
    FORMAT D = spm_eeg_inv_image_display(D,val)  
    Input:  
    D        - input data struct (optional)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_inv_image_display.m)
  """

  return Runtime.call("spm_eeg_inv_image_display", *args, **kwargs, nargout=0)

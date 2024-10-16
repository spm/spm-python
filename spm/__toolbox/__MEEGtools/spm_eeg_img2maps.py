from spm.__wrapper__ import Runtime


def spm_eeg_img2maps(*args, **kwargs):
  """  Make a series of scalp maps from data in an image  
    FORMAT  spm_eeg_img2maps(S)  
     
    S         - input structure (optional)  
    (optional) fields of S:  
       D              - M/EEG dataset containing the sensor locations  
       image          - file name of an image containing M/EEG data in voxel-space  
       window         - start and end of a window in peri-stimulus time [ms]  
       clim           - color limits of the plot  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_img2maps.m)
  """

  return Runtime.call("spm_eeg_img2maps", *args, **kwargs, nargout=0)

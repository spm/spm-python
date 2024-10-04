from spm.__wrap__ import _Runtime


def spm_eeg_mask(*args, **kwargs):
  """  Create a mask image for scalp-level contrasts  
    FORMAT spm_eeg_mask(S)  
     
    S         - input structure (optional)  
    (optional) fields of S:  
       image        - file name of an image containing an unsmoothed   
                      M/EEG data in voxel-space  
       timewin      - start and end of a window in peri-stimulus time [ms]  
       outfile      - output file name  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_mask.m)
  """

  return _Runtime.call("spm_eeg_mask", *args, **kwargs, nargout=0)

from spm.__wrap__ import _Runtime


def spm_eeg_inv_checkdatareg(*args, **kwargs):
  """  Display of the coregistred meshes and sensor locations in MRI space  
    FORMAT spm_eeg_inv_checkdatareg(D, val, ind)  
     
    Fiducials which were used for rigid registration are also displayed.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_inv_checkdatareg.m)
  """

  return _Runtime.call("spm_eeg_inv_checkdatareg", *args, **kwargs, nargout=0)

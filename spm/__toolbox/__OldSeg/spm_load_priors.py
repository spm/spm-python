from spm.__wrap__ import _Runtime


def spm_load_priors(*args, **kwargs):
  """  Load the tissue probability maps for segmentation  
    FORMAT b0 = spm_load_priors(B)  
    B  - structures of image volume information (or filenames)  
    b0 - a cell array of tissue probabilities  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/OldSeg/spm_load_priors.m)
  """

  return _Runtime.call("spm_load_priors", *args, **kwargs)

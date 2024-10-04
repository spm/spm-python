from spm.__wrap__ import _Runtime


def spm_sample_priors(*args, **kwargs):
  """  Sample prior probability maps  
    FORMAT [s,ds1,ds2,ds3] = spm_sample_priors(b,x1,x2,x3,bg)  
    b           - a cell array containing the tissue probability  
                  data (see spm_load_priors)  
    x1,x2,x3    - coordinates to sample  
    bg          - background intensity (i.e. value for points  
                  outside FOV)  
    s           - sampled values  
    ds1,ds2,ds3 - spatial derivatives of sampled values  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/OldSeg/spm_sample_priors.m)
  """

  return _Runtime.call("spm_sample_priors", *args, **kwargs)

from spm.__wrap__ import _Runtime


def spm_cfg_st(*args, **kwargs):
  """  SPM Configuration file for Slice Timing Correction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_st.m)
  """

  return _Runtime.call("spm_cfg_st", *args, **kwargs)

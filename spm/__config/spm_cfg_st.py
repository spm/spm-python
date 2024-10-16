from spm.__wrapper__ import Runtime


def spm_cfg_st(*args, **kwargs):
  """  SPM Configuration file for Slice Timing Correction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_st.m)
  """

  return Runtime.call("spm_cfg_st", *args, **kwargs)

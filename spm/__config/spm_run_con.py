from spm.__wrapper__ import Runtime


def spm_run_con(*args, **kwargs):
  """  SPM job execution function - Specify and estimate contrasts  
    Input:  
    job    - harvested job data structure (see matlabbatch help)  
    Output:  
    out    - struct containing contrast and SPM{.} images filename  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_run_con.m)
  """

  return Runtime.call("spm_run_con", *args, **kwargs)

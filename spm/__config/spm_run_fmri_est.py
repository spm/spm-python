from spm.__wrap__ import _Runtime


def spm_run_fmri_est(*args, **kwargs):
  """  Estimate parameters of a specified model  
    SPM job execution function  
    takes a harvested job data structure and call SPM functions to perform  
    computations on the data.  
    Input:  
    job    - harvested job data structure (see matlabbatch help)  
    Output:  
    out    - computation results, usually a struct variable.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_run_fmri_est.m)
  """

  return _Runtime.call("spm_run_fmri_est", *args, **kwargs)

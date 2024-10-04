from spm.__wrap__ import _Runtime


def spm_fMRI_design_show(*args, **kwargs):
  """  Interactive review of fMRI design matrix  
    FORMAT spm_fMRI_design_show(SPM,s,i)  
     
    Sess(s).U(i)  -  see spm_fMRI_design for session s, trial i.  
     
   _______________________________________________________________________  
    Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/compat/spm_fMRI_design_show.m)
  """

  return _Runtime.call("spm_fMRI_design_show", *args, **kwargs, nargout=0)

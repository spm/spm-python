from spm.__wrapper__ import Runtime


def spm_mb_classes(*args, **kwargs):
  """  Get tissue classes  
    FORMAT [P,dat] = spm_mb_classes(dat,mu,sett)  
    dat  - Data structure for a subject  
    mu   - Warped template data  
    sett - Settings  
    P    - Updated tissue classes  
     
    FORMAT [dat,P] = spm_mb_classes('update_cat',dat,mu,sett)  
    FORMAT l       = spm_mb_classes('LSE0',mu,ax)  
    FORMAT l       = spm_mb_classes('LSE1',mu,ax)  
    FORMAT mu      = spm_mb_classes('template_k1',mu,delta)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_classes.m)
  """

  return Runtime.call("spm_mb_classes", *args, **kwargs)

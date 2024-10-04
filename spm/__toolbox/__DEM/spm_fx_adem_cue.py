from spm.__wrap__ import _Runtime


def spm_fx_adem_cue(*args, **kwargs):
  """  returns the flow for cued response (with action)  
    FORMAT [f]= spm_fx_adem_cue(x,v,a,P)  
     
    x    - hidden states:  
      x.o  - motor angle  
     
    v    - hidden causes  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_adem_cue.m)
  """

  return _Runtime.call("spm_fx_adem_cue", *args, **kwargs)

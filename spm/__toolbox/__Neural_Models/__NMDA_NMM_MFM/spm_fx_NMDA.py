from spm.__wrap__ import _Runtime


def spm_fx_NMDA(*args, **kwargs):
  """  FORMAT [f] = spm_fx_NMDA(x_V,x_G,P,M)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Neural_Models/NMDA_NMM_MFM/spm_fx_NMDA.m)
  """

  return _Runtime.call("spm_fx_NMDA", *args, **kwargs)

from spm.__wrap__ import _Runtime


def spm_mg_switch(*args, **kwargs):
  """  Switching output  
    FORMAT s = spm_mg_switch(V)  
     
    Switching output s: determined by voltage (V) dependent magnesium  
    blockade parameters as per Durstewitz, Seamans & Sejnowski 2000.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_mg_switch.m)
  """

  return _Runtime.call("spm_mg_switch", *args, **kwargs)

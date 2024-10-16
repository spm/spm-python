from spm.__wrapper__ import Runtime


def spm_neil(*args, **kwargs):
  """  Demo routine for hemodynamic model  
   ==========================================================================  
    For Prof Neil Burgess  
    Inst of Cognitive Neuroscience (Deputy Director), and Inst of Neurology  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_neil.m)
  """

  return Runtime.call("spm_neil", *args, **kwargs, nargout=0)

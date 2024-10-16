from spm.__wrapper__ import Runtime


def mci_phase_gx(*args, **kwargs):
  """  Observation function for phase model  
    FORMAT [y,L] = mci_phase_gx (x,u,P,M)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_phase_gx.m)
  """

  return Runtime.call("mci_phase_gx", *args, **kwargs)

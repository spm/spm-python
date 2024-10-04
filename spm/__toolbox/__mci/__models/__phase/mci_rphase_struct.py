from spm.__wrap__ import _Runtime


def mci_rphase_struct(*args, **kwargs):
  """  Initialise weakly coupled oscillator model - reduced connectivity  
    FORMAT [M,U] = mci_rphase_init (d,conn)  
     
    d     number of oscillators  
     
    M     model structure  
    U     inputs  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_rphase_struct.m)
  """

  return _Runtime.call("mci_rphase_init", *args, **kwargs)

from spm.__wrapper__ import Runtime


def mci_rphase_struct(*args, **kwargs):
  """  Initialise weakly coupled oscillator model - reduced connectivity  
    FORMAT [M,U] = mci_rphase_init (d,conn)  
     
    d     number of oscillators  
     
    M     model structure  
    U     inputs  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_rphase_struct.m)
  """

  return Runtime.call("mci_rphase_init", *args, **kwargs)

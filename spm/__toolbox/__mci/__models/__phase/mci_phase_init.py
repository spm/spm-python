from spm.__wrapper__ import Runtime


def mci_phase_init(*args, **kwargs):
  """  Initialise weakly coupled oscillator model  
    FORMAT [P,M,U,Y] = mci_phase_init (d)  
     
    d     number of oscillators  
     
    P     parameters (drawn from prior)  
    M     model structure  
    U     inputs  
    Y     data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_phase_init.m)
  """

  return Runtime.call("mci_phase_init", *args, **kwargs)

from spm._runtime import Runtime


def mci_phase_init(*args, **kwargs):
    r"""
      Initialise weakly coupled oscillator model  
        FORMAT [P,M,U,Y] = mci_phase_init (d)  
         
        d     number of oscillators  
         
        P     parameters (drawn from prior)  
        M     model structure  
        U     inputs  
        Y     data  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/phase/mci_phase_init.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_phase_init", *args, **kwargs)

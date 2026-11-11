from spm._runtime import Runtime


def mci_rphase_struct(*args, **kwargs):
    r"""
      Initialise weakly coupled oscillator model - reduced connectivity  
        FORMAT [M,U] = mci_rphase_init (d,conn)  
         
        d     number of oscillators  
         
        M     model structure  
        U     inputs  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/phase/mci_rphase_struct.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_rphase_init", *args, **kwargs)

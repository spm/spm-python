from spm.__wrapper__ import Runtime


def spm_mfa_demo(*args, **kwargs):
    """
      Demonstration of mean field approximation for spiking neurons.  This demo  
        is just meant to illustrate how one gets from the differential equations  
        of a Hodgkin Huxley like neuron to ensemble dynamics through a Fokker  
        Planck (ensemble density) formulation.  The key to doing this rests on  
        the use of time since last spike as a hidden state (and support of the  
        ensemble density).  This means the ensemble dynamics can be expressed as  
        modes over time, which effectively converts a spiking model into a rate  
        model.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_mfa_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mfa_demo", *args, **kwargs, nargout=0)

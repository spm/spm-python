from spm.__wrapper__ import Runtime


def DEM_self_entropy(*args, **kwargs):
    """
     --------------------------------------------------------------------------  
        Routine to produce graphics illustrating self organisation in terms of  
        the entropy of blanket states and associated trajectories. A low blanket  
        entropy induces anomalous diffusion and itinerancy with power law scaling  
        (i.e., self similar dynamics). This example uses a fixed form (quadratic)  
        likelihood and optimises the density over over hidden states to minimise  
        blanket (i.e., self) entropy explicitly.  
         
        In this example, there is just one active and sensory state and one  
        hidden state to illustrate noise-phase symmetry breaking as the  
        probability density over action reduces the entropy of sensory states  
        under a fixed density of hidden or external states.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_self_entropy.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_self_entropy", *args, **kwargs, nargout=0)

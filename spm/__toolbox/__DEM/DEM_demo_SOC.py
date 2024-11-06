from spm.__wrapper__ import Runtime


def DEM_demo_SOC(*args, **kwargs):
    """
      Demo for a bird songs: this routine illustrates self organised  
        criticality in terms of stimulus induced bifurcations and weak  
        synchronisation of recognition (neuronal) dynamics. It uses the birdsong  
        example, where stimuli are generated using a Lorentz attractor and  
        modelled with the same attractor, with state dependent parameters.  
        These control parameters are categorised in terms of a softmax function  
        of point attractors in a (two-dimensional) perceptual space. We examine  
        the self organised criticality in terms of Lyapunov exponents and the  
        free energy - as a function of precision of the motion of hidden states  
        (see code after return).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_SOC.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_SOC", *args, **kwargs, nargout=0)

from spm.__wrapper__ import Runtime


def DEM_HB_and_LE(*args, **kwargs):
    """
     --------------------------------------------------------------------------  
        This routine is a numerical examination of the relationship between  
        entropy, mutual information and the exponential divergence of  
        trajectories as the Rayleigh parameter of a Lorenz attractoris increased  
        - through a pitchfork bifurcation and subsequent (subcritical) Hopf  
        bifurcation. The (stochastic) Lorentz system is integrated for different  
        values of the Rayleigh parameter. The nonequilibrium steady-state density  
        is then estimated by embedding into a discrete state space; while the  
        bifurcations are characterised in terms of the maximal Lyapunov exponent.  
        The key thing to observe is the decrease in entropy of blanket states  
        prior to the Hopf bifurcation and implicit exponential divergence of  
        trajectories. This is scored by the maximal Lyapunov exponent crossing  
        zero. Here, the form of the Lorenz attractor defines the three states as  
        active, sensory and hidden. Note that there are no internal states in  
        this example and blanket states become the particular states (i.e., the  
        states of a particle).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_HB_and_LE.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_HB_and_LE", *args, **kwargs, nargout=0)

from spm._runtime import Runtime


def ADEM_lorenz_entropy(*args, **kwargs):
    r"""
      This demo shows how structure can be instilled from an environment. It  
        uses an agent that optimises its recognition density over successive  
        epochs of exposure to an environment. This environment causes the agent  
        to flow on a Lorenz attractor with random perturbations. As the agent  
        learns the causal regularities in its environment, it is better able to  
        predict them and act to oppose the random effect. The result is that it  
        is more robust to random forces and therefore exhibits states with lower  
        entropy. This routine takes several minutes to run.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_lorenz_entropy.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_lorenz_entropy", *args, **kwargs, nargout=0)

from spm._runtime import Runtime


def ADEM_lorenz(*args, **kwargs):
    r"""
      Action-DEM demo specifying an attractor (in terms of the parameters of  
        desired equations of motion) This demo first exposes an agent to a Lorenz  
        attractor world such that it can learn the three parameters of the Lorenz  
        system. It is then placed in a test world with a fixed point attractor to  
        see if it has remembered the chaotic dynamics it learnt in the training  
        environment  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_lorenz.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_lorenz", *args, **kwargs, nargout=0)

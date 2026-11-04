from spm._runtime import Runtime


def ADEM_motor(*args, **kwargs):
    r"""
      This demo illustrates how action can fulfil prior expectations by  
        explaining away sensory prediction errors prescribed by desired movement  
        trajectory. It is based on the same linear convolution model of the  
        motor plant considered in the visual tracking example. Here, we induce  
        prediction errors; not through exogenous perturbation to sensory input  
        but through tight priors encoding a desired or expected trajectory. We   
        then show how the movement is robust to changes in the true motor  
        dynamics and other exogenous perturbations, late in movement execution  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/ADEM_motor.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_motor", *args, **kwargs, nargout=0)

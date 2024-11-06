from spm.__wrapper__ import Runtime


def ADEM_motor(*args, **kwargs):
    """
      This demo illustrates how action can fulfil prior expectations by  
        explaining away sensory prediction errors prescribed by desired movement  
        trajectory. It is based on the same linear convolution model of the  
        motor plant considered in the visual tracking example. Here, we induce  
        prediction errors; not through exogenous perturbation to sensory input  
        but through tight priors encoding a desired or expected trajectory. We   
        then show how the movement is robust to changes in the true motor  
        dynamics and other exogenous perturbations, late in movement execution  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_motor.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_motor", *args, **kwargs, nargout=0)

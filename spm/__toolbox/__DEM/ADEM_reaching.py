from spm.__wrapper__ import Runtime


def ADEM_reaching(*args, **kwargs):
    """
      This demo illustrates how action can fulfil prior expectations by  
        explaining away sensory prediction errors prescribed by desired movement  
        trajectories. In this example a two-joint arm is trained to touch a target  
        so that spontaneous reaching occurs after training.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_reaching.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ADEM_reaching", *args, **kwargs, nargout=0)

from spm.__wrapper__ import Runtime


def lbessi(*args, **kwargs):
    """
      GPU single precision f = log(besseli(nu, z))  
        FORMAT f = lbessi(nu,z)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/lbessi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("lbessi", *args, **kwargs)

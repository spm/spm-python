from spm.__wrapper__ import Runtime


def pullg(*args, **kwargs):
    """
      GPU single precision pullg  
        FORMAT g1 = pullg(f0, phi, sett)  
        f0   - 3D float array  
        phi  - 4D float array (dim(4)=3)  
        sett - Settings  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/pullg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pullg", *args, **kwargs)

from spm.__wrapper__ import Runtime


def pull(*args, **kwargs):
    """
      GPU single precision pull  
        FORMAT f1 = pull(f0, phi, sett)  
        f0   - 3D float array  
        phi  - 4D float array (dim(4)=3)  
        sett - Settings  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/pull.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pull", *args, **kwargs)

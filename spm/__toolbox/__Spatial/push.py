from spm.__wrapper__ import Runtime


def push(*args, **kwargs):
    """
      GPU single precision push  
        FORMAT f0 = push(f1, phi, dm0, sett)  
        f1   - 3D float array  
        phi  - 4D float array (dim(4)=3)  
        dm0  - Output dimensions  
        sett - Settings  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/push.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("push", *args, **kwargs)

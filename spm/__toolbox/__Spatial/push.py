from spm._runtime import Runtime


def push(*args, **kwargs):
    r"""
      GPU single precision push  
        FORMAT f0 = push(f1, phi, dm0, sett)  
        f1   - 3D float array  
        phi  - 4D float array (dim(4)=3)  
        dm0  - Output dimensions  
        sett - Settings  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/push.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("push", *args, **kwargs)

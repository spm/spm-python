from spm._runtime import Runtime


def mci_pb_struct(*args, **kwargs):
    r"""
      Preece-Baines model structure  
        FORMAT [M,U] = mci_pb_struct (Nobs)  
         
        Nobs      Number of observations  
         
        M         Model structure  
        U         Input structure  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/growth/mci_pb_struct.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_pb_struct", *args, **kwargs)

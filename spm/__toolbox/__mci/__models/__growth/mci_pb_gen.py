from spm._runtime import Runtime


def mci_pb_gen(*args, **kwargs):
    r"""
      Preece-Baines growth model  
        FORMAT [y] = mci_pb_gen (P,M,U)  
         
        P         parameters  
        M         model  
        U         inputs  
         
        y         time series  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/growth/mci_pb_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_pb_gen", *args, **kwargs)

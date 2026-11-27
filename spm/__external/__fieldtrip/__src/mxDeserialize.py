from spm._runtime import Runtime


def mxDeserialize(*args, **kwargs):
    r"""
      MXDESERIALIZE reconstructs a MATLAB object from a uint8 array suitable  
        for passing down a comms channel to be reconstructed at the other end.  
         
        See also MXSERIALIZE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/mxDeserialize.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mxDeserialize", *args, **kwargs)

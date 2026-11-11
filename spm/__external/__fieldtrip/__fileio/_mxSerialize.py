from spm._runtime import Runtime


def _mxSerialize(*args, **kwargs):
    r"""
      MXSERIALIZE converts any MATLAB object into a uint8 array suitable  
        for passing down a comms channel to be reconstructed at the other end.  
         
        See also MXDESERIALIZE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/mxSerialize.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mxSerialize", *args, **kwargs)

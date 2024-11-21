from spm.__wrapper__ import Runtime


def _mxDeserialize(*args, **kwargs):
    """
      MXDESERIALIZE reconstructs a MATLAB object from a uint8 array suitable  
        for passing down a comms channel to be reconstructed at the other end.  
         
        See also MXSERIALIZE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/mxDeserialize.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mxDeserialize", *args, **kwargs)

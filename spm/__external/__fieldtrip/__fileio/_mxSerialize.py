from spm._runtime import Runtime


def _mxSerialize(*args, **kwargs):
    """
      MXSERIALIZE converts any MATLAB object into a uint8 array suitable  
        for passing down a comms channel to be reconstructed at the other end.  
         
        See also MXDESERIALIZE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/mxSerialize.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mxSerialize", *args, **kwargs)

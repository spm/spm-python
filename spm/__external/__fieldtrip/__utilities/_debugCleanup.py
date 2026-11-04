from spm._runtime import Runtime


def _debugCleanup(*args, **kwargs):
    r"""
      DEBUGCLEANUP is a cleanup function that is being used by FT_PREAMBLE_DEBUG. It is  
        called when a high-level FieldTrip function exits, either after finishing successfully or after detecting an error.  
         
        See also FT_PREAMBLE_DEBUG, FT_POSTAMBLE_DEBUG  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/debugCleanup.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("debugCleanup", *args, **kwargs, nargout=0)

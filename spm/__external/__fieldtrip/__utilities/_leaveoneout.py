from spm._runtime import Runtime


def _leaveoneout(*args, **kwargs):
    r"""
    leaveoneout is a function.  
          data = leaveoneout(data)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/leaveoneout.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("leaveoneout", *args, **kwargs)

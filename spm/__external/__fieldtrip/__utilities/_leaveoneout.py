from spm.__wrapper__ import Runtime


def _leaveoneout(*args, **kwargs):
    """
    leaveoneout is a function.  
          data = leaveoneout(data)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/leaveoneout.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("leaveoneout", *args, **kwargs)

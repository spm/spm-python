from spm._runtime import Runtime


def _smartinput(*args, **kwargs):
    r"""
      SMARTINPUT helper function for smart interactive input from the command line  
         
        Use as  
          [newval, change] = smartinput(question, oldval)  
         
        See also INPUT, PAUSE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/smartinput.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("smartinput", *args, **kwargs)

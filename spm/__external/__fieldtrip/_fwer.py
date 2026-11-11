from spm._runtime import Runtime


def _fwer(*args, **kwargs):
    r"""
      FWER family-wise error rate control using Bonferoni method  
         
        Use as  
          h = fwer(p, q)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/fwer.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fwer", *args, **kwargs)

from spm._runtime import Runtime


def boxcar(*args, **kwargs):
    r"""
      BOXCAR returns a boxcar taper  
         
        Use as  
          w = boxcar(n)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/signal/boxcar.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("boxcar", *args, **kwargs)

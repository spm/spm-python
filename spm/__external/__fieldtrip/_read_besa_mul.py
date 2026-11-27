from spm._runtime import Runtime


def _read_besa_mul(*args, **kwargs):
    r"""
      READ_BESA_MUL reads data from a BESA multiplexed (*.mul) file  
         
        Use as  
          dat = read_besa_mul(filename);  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/read_besa_mul.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_besa_mul", *args, **kwargs)

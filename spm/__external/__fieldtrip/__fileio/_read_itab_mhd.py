from spm._runtime import Runtime


def _read_itab_mhd(*args, **kwargs):
    r"""
    read_itab_mhd is a function.  
          mhd = read_itab_mhd(filename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_itab_mhd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_itab_mhd", *args, **kwargs)

from spm._runtime import Runtime


def _read_bti_m4d(*args, **kwargs):
    r"""
      READ_BTI_M4D  
         
        Use as  
          msi = read_bti_m4d(filename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_bti_m4d.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_bti_m4d", *args, **kwargs)

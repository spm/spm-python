from spm._runtime import Runtime


def _read_tck(*args, **kwargs):
    r"""
      READ_TCK reads tractography information from an mrtrix-generated .tck  
        file. Requires the matlab functions from mrtrix.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_tck.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_tck", *args, **kwargs)

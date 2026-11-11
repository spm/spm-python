from spm._runtime import Runtime


def _read_ah5_markers(*args, **kwargs):
    r"""
    read_ah5_markers is a function.  
          [event] = read_ah5_markers(hdr, filename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_ah5_markers.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ah5_markers", *args, **kwargs)

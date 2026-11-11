from spm._runtime import Runtime


def _read_off(*args, **kwargs):
    r"""
      READ_OFF reads vertices and triangles from a OFF format triangulation file  
         
        [pnt, tri] = read_off(filename)  
         
        See also READ_TRI, READ_BND  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_off.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_off", *args, **kwargs)

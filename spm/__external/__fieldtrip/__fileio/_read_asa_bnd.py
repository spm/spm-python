from spm._runtime import Runtime


def _read_asa_bnd(*args, **kwargs):
    r"""
      READ_ASA_BND reads an ASA boundary triangulation file  
        converting the units of the vertices to mm  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_asa_bnd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_asa_bnd", *args, **kwargs)

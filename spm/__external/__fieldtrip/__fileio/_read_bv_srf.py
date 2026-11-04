from spm._runtime import Runtime


def _read_bv_srf(*args, **kwargs):
    r"""
      READ_BV_SRF reads a triangulated surface from a BrainVoyager *.srf file  
         
        Use as  
          [pnt, tri] = read_bv_srf(filename) or  
          [pnt, tri, srf] = read_bv_srf(filename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_bv_srf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_bv_srf", *args, **kwargs)

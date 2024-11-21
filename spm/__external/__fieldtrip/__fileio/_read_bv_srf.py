from spm.__wrapper__ import Runtime


def _read_bv_srf(*args, **kwargs):
    """
      READ_BV_SRF reads a triangulated surface from a BrainVoyager *.srf file  
         
        Use as  
          [pnt, tri] = read_bv_srf(filename) or  
          [pnt, tri, srf] = read_bv_srf(filename)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_bv_srf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_bv_srf", *args, **kwargs)

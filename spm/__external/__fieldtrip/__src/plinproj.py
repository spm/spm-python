from spm._runtime import Runtime


def plinproj(*args, **kwargs):
    r"""
      PLINPROJ projects a point onto a line or linepiece  
         
        Use as  
          [proj, dist] = plinproj(l1, l2, r, flag)  
        where l1 and l2 are the begin and endpoint of the linepiece, and r is  
        the point that is projected onto the line  
         
        the optional flag can be:  
          0 (default)  project the point anywhere on the complete line  
          1            project the point within or on the edge of the linepiece  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/plinproj.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("plinproj", *args, **kwargs)

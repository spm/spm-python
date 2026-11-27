from spm._runtime import Runtime


def _plinprojn(*args, **kwargs):
    r"""
      PLINPROJN projects a point onto a line or linepiece  
         
        [proj, dist] = plinprojn(l1, l2, r, flag)  
          
        where l1 and l2 are Nx3 matrices with the begin and endpoints of the linepieces,   
        and r is the point that is projected onto the lines  
        This is a vectorized version of Robert's plinproj function and is  
        generally faster than a for-loop around the mex-file.  
         
        the optional flag can be:  
          0 (default)  project the point anywhere on the complete line  
          1            project the point within or on the edge of the linepiece  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/plinprojn.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("plinprojn", *args, **kwargs)

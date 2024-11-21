from spm.__wrapper__ import Runtime


def _plinprojn(*args, **kwargs):
    """
      PLINPROJN projects a point onto a line or linepiece  
         
        [proj, dist] = plinprojn(l1, l2, r, flag)  
          
        where l1 and l2 are Nx3 matrices with the begin and endpoints of the linepieces,   
        and r is the point that is projected onto the lines  
        This is a vectorized version of Robert's plinproj function and is  
        generally faster than a for-loop around the mex-file.  
         
        the optional flag can be:  
          0 (default)  project the point anywhere on the complete line  
          1            project the point within or on the edge of the linepiece  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/plinprojn.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("plinprojn", *args, **kwargs)

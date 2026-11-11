from spm._runtime import Runtime


def _ptriside(*args, **kwargs):
    r"""
      PTRISIDE determines the side of a plane on which a set of points lie. It  
        returns 0 for the points that lie exactly on the plane.  
         
        [side] = ptriside(v1, v2, v3, r)  
          
        the side of points r is determined relative to the plane spanned by  
        vertices v1, v2 and v3. v1,v2 and v3 should be 1x3 vectors. r should be a  
        Nx3 matrix  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/ptriside.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ptriside", *args, **kwargs)

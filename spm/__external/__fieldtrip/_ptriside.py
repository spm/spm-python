from spm.__wrapper__ import Runtime


def _ptriside(*args, **kwargs):
    """
      PTRISIDE determines the side of a plane on which a set of points lie. It  
        returns 0 for the points that lie exactly on the plane.  
         
        [side] = ptriside(v1, v2, v3, r)  
          
        the side of points r is determined relative to the plane spanned by  
        vertices v1, v2 and v3. v1,v2 and v3 should be 1x3 vectors. r should be a  
        Nx3 matrix  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/ptriside.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ptriside", *args, **kwargs)

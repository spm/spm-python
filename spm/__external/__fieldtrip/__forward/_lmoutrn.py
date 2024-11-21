from spm.__wrapper__ import Runtime


def _lmoutrn(*args, **kwargs):
    """
      LMOUTRN computes the la/mu parameters of a point projected to triangles  
         
        Use as  
          [la, mu, dist, proj] = lmoutrn(v1, v2, v3, r)  
        where v1, v2 and v3 are Nx3 matrices with vertex positions of the triangles,   
        and r is the point that is projected onto the planes spanned by the vertices  
        This is a vectorized version of Robert's lmoutrn function and is  
        generally faster than a for-loop around the mex-file. It also returns the   
        projection of the point r onto the planes of the triangles, and the signed  
        distance to the triangles. The sign of the distance is negative if the point  
        lies closer to the average across all vertices and the triangle under consideration.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/lmoutrn.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("lmoutrn", *args, **kwargs)

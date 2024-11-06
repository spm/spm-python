from spm.__wrapper__ import Runtime


def _ptriprojn(*args, **kwargs):
    """
      PTRIPROJN projects a point onto the plane going through a set of  
        triangles  
         
        Use as  
          [proj, dist] = ptriprojn(v1, v2, v3, r, flag)  
        where v1, v2 and v3 are Nx3 matrices with vertex positions of the triangles,   
        and r is the point that is projected onto the planes spanned by the vertices  
        This is a vectorized version of Robert's ptriproj function and is  
        generally faster than a for-loop around the mex-file.  
         
        the optional flag can be:  
          0 (default)  project the point anywhere on the complete plane  
          1            project the point within or on the edge of the triangle  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ptriprojn.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ptriprojn", *args, **kwargs)

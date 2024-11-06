from spm.__wrapper__ import Runtime


def _ptriproj(*args, **kwargs):
    """
      PTRIPROJ projects a point onto the plane going through a triangle  
         
        Use as  
          [proj, dist] = ptriproj(v1, v2, v3, r, flag)  
        where v1, v2 and v3 are three vertices of the triangle, and r is   
        the point that is projected onto the plane spanned by the vertices  
         
        the optional flag can be:  
          0 (default)  project the point anywhere on the complete plane  
          1            project the point within or on the edge of the triangle  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/ptriproj.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ptriproj", *args, **kwargs)

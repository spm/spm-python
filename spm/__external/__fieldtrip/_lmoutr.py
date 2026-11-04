from spm._runtime import Runtime


def _lmoutr(*args, **kwargs):
    r"""
      LMOUTR computes the la/mu parameters of a point projected to a triangle  
         
        Use as  
          [la, mu, dist] = lmoutr(v1, v2, v3, r)  
        where v1, v2 and v3 are three vertices of the triangle, and r is  
        the point that is projected onto the plane spanned by the vertices  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/lmoutr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("lmoutr", *args, **kwargs)

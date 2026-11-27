from spm._runtime import Runtime


def routlm(*args, **kwargs):
    r"""
      ROUTLM computes the projection of a point from its la/mu parameters  
        these equal the "Barycentric" coordinates  
         
        Use as  
          [proj] = routlm(v1, v2, v3, la, mu)  
        where v1, v2 and v3 are three vertices of the triangle  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/routlm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("routlm", *args, **kwargs)

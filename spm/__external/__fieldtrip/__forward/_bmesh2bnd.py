from spm._runtime import Runtime


def _bmesh2bnd(*args, **kwargs):
    r"""
      Helper to convert the fieldtrip bnd format for meshes into the bmesh  
        format for the HBF toolbox, and vice versa.  
         
        George O'Neill  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/bmesh2bnd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bmesh2bnd", *args, **kwargs)

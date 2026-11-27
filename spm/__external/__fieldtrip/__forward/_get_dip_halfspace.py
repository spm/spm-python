from spm._runtime import Runtime


def _get_dip_halfspace(*args, **kwargs):
    r"""
      GET_DIP_HALFSPACE checks if the dipole is in the empty halfspace and  
        returns true if this happens. The normal of the plane points by  
        convention to the empty halfspace.  
                
        is_in_empty = get_dip_halfspace(P,vol);  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/get_dip_halfspace.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("get_dip_halfspace", *args, **kwargs)

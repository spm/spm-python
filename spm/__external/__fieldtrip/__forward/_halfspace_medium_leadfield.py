from spm._runtime import Runtime


def _halfspace_medium_leadfield(*args, **kwargs):
    r"""
      HALFSPACE_MEDIUM_LEADFIELD calculate the halfspace medium leadfield  
        on positions pnt for a dipole at position rd and conductivity cond  
        The halfspace solution requires a plane dividing a conductive zone of  
        conductivity cond, from a non coductive zone (cond = 0)  
                
        [lf] = halfspace_medium_leadfield(rd, elc, cond)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/halfspace_medium_leadfield.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("halfspace_medium_leadfield", *args, **kwargs)

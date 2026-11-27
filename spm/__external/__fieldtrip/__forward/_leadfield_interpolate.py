from spm._runtime import Runtime


def _leadfield_interpolate(*args, **kwargs):
    r"""
      LEADFIELD_INTERPOLATE interpolates the leadfield for a source at  
        an arbitrary location given the pre-computed leadfields on a regular  
        grid.  
         
        Use as  
          lf = leadfield_interpolate(pos, vol)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/leadfield_interpolate.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("leadfield_interpolate", *args, **kwargs)

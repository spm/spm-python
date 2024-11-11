from spm.__wrapper__ import Runtime


def _leadfield_interpolate(*args, **kwargs):
    """
      LEADFIELD_INTERPOLATE interpolates the leadfield for a source at  
        an arbitrary location given the pre-computed leadfields on a regular  
        grid.  
         
        Use as  
          lf = leadfield_interpolate(pos, vol)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/leadfield_interpolate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("leadfield_interpolate", *args, **kwargs)

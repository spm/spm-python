from spm._runtime import Runtime


def _magnetic_dipole(*args, **kwargs):
    r"""
      MAGNETIC_DIPOLE leadfield for a magnetic dipole in an infinite medium  
         
        [lf] = magnetic_dipole(R, pos, ori)  
         
        with input arguments  
          R           position dipole  
          pos         position magnetometers  
          ori         orientation magnetometers  
         
        See also CURRENT_DIPOLE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/magnetic_dipole.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("magnetic_dipole", *args, **kwargs)

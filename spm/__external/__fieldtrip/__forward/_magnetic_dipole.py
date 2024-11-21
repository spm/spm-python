from spm.__wrapper__ import Runtime


def _magnetic_dipole(*args, **kwargs):
    """
      MAGNETIC_DIPOLE leadfield for a magnetic dipole in an infinite medium  
         
        [lf] = magnetic_dipole(R, pos, ori)  
         
        with input arguments  
          R           position dipole  
          pos         position magnetometers  
          ori         orientation magnetometers  
         
        See also CURRENT_DIPOLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/magnetic_dipole.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("magnetic_dipole", *args, **kwargs)

from spm.__wrapper__ import Runtime


def _current_dipole(*args, **kwargs):
    """
      CURRENT_DIPOLE leadfield for a current dipole in an infinite homogenous medium  
         
        [lf] = current_dipole(R, pos, ori)  
         
        with input arguments  
          R           position dipole  
          pos         position magnetometers  
          ori         orientation magnetometers  
         
        This implements equation 9.3-1 from R.M. Gulrajani (1998) Bioelectricity and  
        Biomagnetism, John Wiley and Sons, ISBN 04712485252.  
         
        See also MAGNETIC_DIPOLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/current_dipole.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("current_dipole", *args, **kwargs)

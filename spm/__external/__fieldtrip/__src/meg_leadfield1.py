from spm.__wrapper__ import Runtime


def meg_leadfield1(*args, **kwargs):
    """
      MEG_LEADFIELD1 magnetic leadfield for a dipole in a homogenous sphere  
         
        [lf] = meg_leadfield1(R, pos, ori)  
         
        with input arguments  
          R         position dipole  
          pos     position magnetometers  
          ori     orientation magnetometers  
         
        The center of the homogenous sphere is in the origin, the field  
        of the dipole is not dependent on the sphere radius.  
         
        This function is also implemented as MEX file.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/meg_leadfield1.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("meg_leadfield1", *args, **kwargs)

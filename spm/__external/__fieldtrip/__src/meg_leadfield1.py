from spm._runtime import Runtime


def meg_leadfield1(*args, **kwargs):
    r"""
      MEG_LEADFIELD1 magnetic leadfield for a dipole in a homogenous sphere  
         
        Use as  
          [lf] = meg_leadfield1(dippos, coilpos, coilori)  
        with input arguments  
          dippos    position of the dipole dipole  
          coilpos   position of the magnetometers  
          coilori   orientation of the magnetometers  
         
        The center of the homogenous sphere is in the origin, the field  
        of the dipole is not dependent on the sphere radius.  
         
        This function is also implemented as MEX file.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/meg_leadfield1.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("meg_leadfield1", *args, **kwargs)

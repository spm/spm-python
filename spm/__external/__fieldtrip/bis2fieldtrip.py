from spm._runtime import Runtime


def bis2fieldtrip(*args, **kwargs):
    r"""
      BIS2FIELDTRIP reads BioImage Suite .mgrid files and converts them   
        into a FieldTrip-compatible elec datatype structure and converts electrode  
        positions from BioImage Suite mgrid that are in 'xyz' to head coordinates  
        of the corresponding MRI volume   
         
        Use as  
          elec = bis2fieldtrip('Subject_grid.mgrid', 'Subject_MR.nii')  
         
        See also FIELDTRIP2BIS, FT_READ_SENS, READ_BIOIMAGE_MGRID  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/bis2fieldtrip.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bis2fieldtrip", *args, **kwargs)

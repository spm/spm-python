from spm._runtime import Runtime


def fieldtrip2bis(*args, **kwargs):
    r"""
      FIELDTRIP2BIS writes BioImage Suite .mgrid files with eletrode   
        positions in 'xyz' coordinates using a elec datatype structure and the   
        corresponding MRI volume   
         
        Use as  
          fieldtrip2bis('Subject_grid.mgrid', elec, 'Subject_MR.nii')  
         
        See also BIS2FIELDTRIP, FT_WRITE_SENS, WRITE_BIOIMAGE_MGRID  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fieldtrip2bis.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fieldtrip2bis", *args, **kwargs, nargout=0)

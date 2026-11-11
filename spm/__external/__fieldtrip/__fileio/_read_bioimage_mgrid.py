from spm._runtime import Runtime


def _read_bioimage_mgrid(*args, **kwargs):
    r"""
      READ_BIOIMAGE_MGRID reads BioImage Suite *.mgrid files and converts them  
        into a FieldTrip-compatible elec datatype structure with electrode  
        positions in xyz coordinates (equals voxel coordinates in mm)  
         
        Use as  
          elec = read_bioimage_mgrid(filename)  
        where the filename has the .mgrid file extension  
         
        See also FT_READ_SENS, FT_DATATYPE_SENS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_bioimage_mgrid.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_bioimage_mgrid", *args, **kwargs)

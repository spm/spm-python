from spm.__wrapper__ import Runtime


def _read_bioimage_mgrid(*args, **kwargs):
    """
      READ_BIOIMAGE_MGRID reads BioImage Suite *.mgrid files and converts them  
        into a FieldTrip-compatible elec datatype structure with electrode  
        positions in xyz coordinates (equals voxel coordinates in mm)  
         
        Use as  
          elec = read_bioimage_mgrid(filename)  
        where the filename has the .mgrid file extension  
         
        See also FT_READ_SENS, FT_DATATYPE_SENS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_bioimage_mgrid.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_bioimage_mgrid", *args, **kwargs)

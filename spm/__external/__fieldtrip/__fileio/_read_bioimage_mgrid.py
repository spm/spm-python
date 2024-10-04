from spm.__wrap__ import _Runtime


def _read_bioimage_mgrid(*args, **kwargs):
  """  READ_BIOIMAGE_MGRID reads BioImage Suite *.mgrid files and converts them  
    into a FieldTrip-compatible elec datatype structure with electrode  
    positions in xyz coordinates (equals voxel coordinates in mm)  
     
    Use as  
      elec = read_bioimage_mgrid(filename)  
    where the filename has the .mgrid file extension  
     
    See also FT_READ_SENS, FT_DATATYPE_SENS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_bioimage_mgrid.m)
  """

  return _Runtime.call("read_bioimage_mgrid", *args, **kwargs)

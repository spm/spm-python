from spm.__wrap__ import _Runtime


def _read_yorkinstruments_hdf5_meta(*args, **kwargs):
  """  READ_YPRKINSTRUMENTS_HDF5_META reads the metatada and header information from a .meghdf5 file  
     
    Use as  
      info=read_yorkinstruments_hdf5_meta(datafile)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_yorkinstruments_hdf5_meta.m)
  """

  return _Runtime.call("read_yorkinstruments_hdf5_meta", *args, **kwargs)

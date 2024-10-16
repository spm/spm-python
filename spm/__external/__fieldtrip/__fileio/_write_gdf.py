from spm.__wrapper__ import Runtime


def _write_gdf(*args, **kwargs):
  """  WRITE_GDF(filename, header, data)  
     
    Writes a GDF file from the given header (only label, Fs, nChans are of interest)  
    and the data (unmodified). Digital and physical limits are derived from the data  
    via min and max operators. The GDF file will contain N records of 1 sample each,  
    where N is the number of columns in 'data'.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_gdf.m)
  """

  return Runtime.call("write_gdf", *args, **kwargs, nargout=0)

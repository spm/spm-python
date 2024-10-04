from spm.__wrap__ import _Runtime


def fiff_read_hpi_result(*args, **kwargs):
  """   
    [ res ] = fiff_read_hpi_result(name)  
     
    Read the HPI result block from a measurement file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_hpi_result.m)
  """

  return _Runtime.call("fiff_read_hpi_result", *args, **kwargs)

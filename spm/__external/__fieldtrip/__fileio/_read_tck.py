from spm.__wrap__ import _Runtime


def _read_tck(*args, **kwargs):
  """  READ_TCK reads tractography information from an mrtrix-generated .tck  
    file. Requires the matlab functions from mrtrix.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_tck.m)
  """

  return _Runtime.call("read_tck", *args, **kwargs)

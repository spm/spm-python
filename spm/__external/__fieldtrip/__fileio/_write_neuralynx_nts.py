from spm.__wrap__ import _Runtime


def _write_neuralynx_nts(*args, **kwargs):
  """  WRITE_NEURALYNX_NTS writes spike timestamps to a NTS file  
     
    Use as  
      write_neuralynx_nts(filename, nts)  
     
    See also READ_NEURALYNX_NTS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_neuralynx_nts.m)
  """

  return _Runtime.call("write_neuralynx_nts", *args, **kwargs, nargout=0)

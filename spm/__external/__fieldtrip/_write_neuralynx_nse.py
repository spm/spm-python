from spm.__wrap__ import _Runtime


def _write_neuralynx_nse(*args, **kwargs):
  """  WRITE_NEURALYNX_NSE writes spike timestamps and waveforms to a NSE file  
    The input data should be scaled in uV.  
     
    Use as  
      write_neuralynx_nse(filename, nse)  
     
    See also READ_NEURALYNX_NSE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/write_neuralynx_nse.m)
  """

  return _Runtime.call("write_neuralynx_nse", *args, **kwargs, nargout=0)

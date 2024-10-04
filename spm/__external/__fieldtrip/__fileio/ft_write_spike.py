from spm.__wrap__ import _Runtime


def ft_write_spike(*args, **kwargs):
  """  FT_WRITE_SPIKE writes animal electrophysiology spike timestamps and/or waveforms  
    to file  
     
    Use as  
      ft_write_spike(filename, spike, ...)  
     
    Additional options should be specified in key-value pairs and can be  
      'dataformat'          string, see below  
      'fsample'             sampling frequency of the waveforms  
      'chanindx'            index of selected channels  
      'TimeStampPerSample'  number of timestamps per sample  
     
    The supported dataformats are  
      neuralynx_nse  
      neuralynx_nts  
      plexon_nex  
      matlab  
     
    See also FT_READ_SPIKE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_write_spike.m)
  """

  return _Runtime.call("ft_write_spike", *args, **kwargs, nargout=0)

from spm.__wrapper__ import Runtime


def _read_neuralynx_nts(*args, **kwargs):
  """  READ_NEURALYNX_NTS reads spike timestamps  
     
    Use as  
      [nts] = read_neuralynx_nts(filename)  
      [nts] = read_neuralynx_nts(filename, begrecord, endrecord)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_nts.m)
  """

  return Runtime.call("read_neuralynx_nts", *args, **kwargs)

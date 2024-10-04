from spm.__wrap__ import _Runtime


def _read_neuralynx_ntt(*args, **kwargs):
  """  READ_NEURALYNX_NTT reads a single tetrode file  
     
    Use as  
      [ntt] = read_neuralynx_ntt(filename)  
      [ntt] = read_neuralynx_ntt(filename, begrecord, endrecord)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_ntt.m)
  """

  return _Runtime.call("read_neuralynx_ntt", *args, **kwargs)

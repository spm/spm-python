from spm.__wrap__ import _Runtime


def _read_neuralynx_nst(*args, **kwargs):
  """  READ_NEURALYNX_NST reads a single stereotrode file  
     
    Use as  
      [nst] = read_neuralynx_nst(filename)  
      [nst] = read_neuralynx_nst(filename, begrecord, endrecord)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_nst.m)
  """

  return _Runtime.call("read_neuralynx_nst", *args, **kwargs)

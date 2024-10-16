from spm.__wrapper__ import Runtime


def _read_neuralynx_ncs(*args, **kwargs):
  """  READ_NEURALYNX_NCS reads a single continuous channel file  
     
    Use as  
      [ncs] = read_neuralynx_ncs(filename)  
      [ncs] = read_neuralynx_ncs(filename, begrecord, endrecord)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_ncs.m)
  """

  return Runtime.call("read_neuralynx_ncs", *args, **kwargs)

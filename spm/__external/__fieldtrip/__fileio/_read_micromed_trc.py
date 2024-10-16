from spm.__wrapper__ import Runtime


def _read_micromed_trc(*args, **kwargs):
  """ --------------------------------------------------------------------------  
    reads Micromed .TRC file into matlab, version Mariska, edited by Romain  
    input: filename  
    output: datamatrix  
   --------------------------------------------------------------------------  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_micromed_trc.m)
  """

  return Runtime.call("read_micromed_trc", *args, **kwargs)

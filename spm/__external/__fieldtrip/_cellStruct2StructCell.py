from spm.__wrapper__ import Runtime


def _cellStruct2StructCell(*args, **kwargs):
  """  Converts a cell-array of structure arrays into a structure array  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/cellStruct2StructCell.m)
  """

  return Runtime.call("cellStruct2StructCell", *args, **kwargs)

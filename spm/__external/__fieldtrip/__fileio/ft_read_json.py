from spm.__wrap__ import _Runtime


def ft_read_json(*args, **kwargs):
  """  FT_READ_JSON reads information from a JSON file and represents it as a MATLAB structure  
     
    Use as  
      json = ft_read_json(filename)  
     
    See also FT_WRITE_JSON, FT_READ_TSV, FT_WRITE_TSV, JSONDECODE, JSONENCODE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_read_json.m)
  """

  return _Runtime.call("ft_read_json", *args, **kwargs)

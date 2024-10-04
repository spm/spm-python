from spm.__wrap__ import _Runtime


def ft_write_tsv(*args, **kwargs):
  """  FT_WRITE_TSV writes a MATLAB table to a tab-separated-values file. Compared to the  
    builtin MATLAB function, this implementation deals a bit different with missing  
    values, booleans, and NaNs.  
     
    Use as  
      ft_write_tsv(filename, table)  
     
    See also FT_READ_TSV, FT_READ_JSON, FT_WRITE_JSON, READTABLE, WRITETABLE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_write_tsv.m)
  """

  return _Runtime.call("ft_write_tsv", *args, **kwargs, nargout=0)

from spm.__wrap__ import _Runtime


def ft_source2grid(*args, **kwargs):
  """  FT_SOURCE2GRID removes the fields from a source structure that are  
    not necessary to reuse the dipole grid in another source estimation.  
     
    Use as  
      [grid] = ft_source2grid(source);  
     
    The resulting grid can be used in the configuration of another  
    run of FT_SOURCEANALYSIS.  
     
    See also FTSOURCE2SPARSE, FT_SOURCE2FULL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_source2grid.m)
  """

  return _Runtime.call("ft_source2grid", *args, **kwargs)

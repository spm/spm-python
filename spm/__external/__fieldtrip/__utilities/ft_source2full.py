from spm.__wrap__ import _Runtime


def ft_source2full(*args, **kwargs):
  """  FT_SOURCE2FULL recreates the grid locations outside the brain in the source  
    reconstruction, so that the source volume again describes the full grid.  
    This undoes the memory savings that can be achieved using FT_SOURCE2SPARSE  
    and makes it possible again to plot the source volume and save it to an  
    external file.  
     
    Use as  
      [source] = ft_source2full(source)  
     
    See also FT_SOURCE2SPARSE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_source2full.m)
  """

  return _Runtime.call("ft_source2full", *args, **kwargs)

from spm.__wrapper__ import Runtime


def _open_figure(*args, **kwargs):
  """  OPEN_FIGURE is a helper function to open a figure with some specific settings  
    consistent over all FieldTrip functions that do plotting and/or that show a  
    graphical user interface.  
     
    See also GCA, GCF, GROOT,  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/open_figure.m)
  """

  return Runtime.call("open_figure", *args, **kwargs)

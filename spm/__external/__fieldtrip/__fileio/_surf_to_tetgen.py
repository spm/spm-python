from spm.__wrap__ import _Runtime


def _surf_to_tetgen(*args, **kwargs):
  """  This function converts a triangulated mesh in FieldTrip format into a  
    surface structure readable by Tetgen software  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/surf_to_tetgen.m)
  """

  return _Runtime.call("surf_to_tetgen", *args, **kwargs, nargout=0)

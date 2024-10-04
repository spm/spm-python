from spm.__wrap__ import _Runtime


def _uidisplaytext(*args, **kwargs):
  """  UIDISPLAYTEXT opens a figure for displaying multi-line text  
    in an "edit" user interface control element.  
     
    Use as  
      uidisplaytext(str, title)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/uidisplaytext.m)
  """

  return _Runtime.call("uidisplaytext", *args, **kwargs, nargout=0)

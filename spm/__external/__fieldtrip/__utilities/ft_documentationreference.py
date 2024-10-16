from spm.__wrapper__ import Runtime


def ft_documentationreference(*args, **kwargs):
  """  FT_DOCUMENTATIONREFERENCE is a helper function to maintain the  
    online reference documentation.  
     
    Normal users will not be calling this function, but will rather look at  
    http://www.fieldtriptoolbox.org/reference where the output of this function can  
    be found.  
     
    See also FT_DOCUMENTATIONCONFIGURATION, MATLAB2MARKDOWN  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_documentationreference.m)
  """

  return Runtime.call("ft_documentationreference", *args, **kwargs, nargout=0)

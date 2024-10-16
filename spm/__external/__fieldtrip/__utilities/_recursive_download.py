from spm.__wrapper__ import Runtime


def _recursive_download(*args, **kwargs):
  """  RECURSIVE_DOWNLOAD downloads a complete directory from a RESTful web service  
     
    Use as  
      recursive_download(webLocation, localFolder)  
     
    See also WEBREAD, WEBSAVE, UNTAR, UNZIP, GUNZIP  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/recursive_download.m)
  """

  return Runtime.call("recursive_download", *args, **kwargs, nargout=0)

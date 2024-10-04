from spm.__wrap__ import _Runtime


def _fetch_url(*args, **kwargs):
  """  FETCH_URL checks the filename and downloads the file to a local copy in  
    case it is specified as an Universal Resource Locator. It returns the  
    name of the temporary file on the local filesystem.  
     
    Use as  
      filename = fetch_url(filename)  
     
    In case the filename does not specify an URL, it just returns the original  
    filename.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/fetch_url.m)
  """

  return _Runtime.call("fetch_url", *args, **kwargs)

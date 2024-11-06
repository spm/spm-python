from spm.__wrapper__ import Runtime


def _fetch_url(*args, **kwargs):
    """
      FETCH_URL checks the filename and downloads the file to a local copy in  
        case it is specified as an Universal Resource Locator. It returns the  
        name of the temporary file on the local filesystem.  
         
        Use as  
          filename = fetch_url(filename)  
         
        In case the filename does not specify an URL, it just returns the original  
        filename.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/fetch_url.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fetch_url", *args, **kwargs)

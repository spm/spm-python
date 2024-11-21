from spm.__wrapper__ import Runtime


def _recursive_download(*args, **kwargs):
    """
      RECURSIVE_DOWNLOAD downloads a complete directory from a RESTful web service  
         
        Use as  
          recursive_download(webLocation, localFolder)  
         
        See also WEBREAD, WEBSAVE, UNTAR, UNZIP, GUNZIP  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/recursive_download.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("recursive_download", *args, **kwargs, nargout=0)

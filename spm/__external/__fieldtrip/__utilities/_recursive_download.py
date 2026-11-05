from spm._runtime import Runtime


def _recursive_download(*args, **kwargs):
    r"""
      RECURSIVE_DOWNLOAD downloads a complete directory from a RESTful web service  
         
        Use as  
          recursive_download(webLocation, localFolder)  
         
        See also WEBREAD, WEBSAVE, UNTAR, UNZIP, GUNZIP  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/recursive_download.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("recursive_download", *args, **kwargs, nargout=0)

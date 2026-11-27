from spm._runtime import Runtime


def _np_read_splitted_fileinfo(*args, **kwargs):
    r"""
       
        function [np_info] = np_read_splitted_fileinfo (filename, option)  
         
        This function is necessary for np_readfileinfo.m.  
         
        eldith GmbH  
        Gustav-Kirchhoff-Str. 5  
        D-98693 Ilmenau  
        Germany  
        02.02.2005  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/np_read_splitted_fileinfo.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("np_read_splitted_fileinfo", *args, **kwargs)

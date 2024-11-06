from spm.__wrapper__ import Runtime


def _np_read_splitted_fileinfo(*args, **kwargs):
    """
       
        function [np_info] = np_read_splitted_fileinfo (filename, option)  
         
        This function is necessary for np_readfileinfo.m.  
         
        eldith GmbH  
        Gustav-Kirchhoff-Str. 5  
        D-98693 Ilmenau  
        Germany  
        02.02.2005  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/np_read_splitted_fileinfo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("np_read_splitted_fileinfo", *args, **kwargs)

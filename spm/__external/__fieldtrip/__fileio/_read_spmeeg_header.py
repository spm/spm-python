from spm._runtime import Runtime


def _read_spmeeg_header(*args, **kwargs):
    r"""
      read_spmeeg_header() - import SPM5 and SPM8 meeg datasets  
         
        Usage:  
          >> header = read_spmeeg_header(filename);  
         
        Inputs:  
          filename - [string] file name  
         
        Outputs:  
          header   - FILEIO toolbox type structure  
        _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
        Vladimir Litvak  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_spmeeg_header.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_spmeeg_header", *args, **kwargs)

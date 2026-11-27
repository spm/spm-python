from spm._runtime import Runtime


def _read_buffer_offline_header(*args, **kwargs):
    r"""
      function [hdr, nameFlag] = read_buffer_offline_header(headerfile)  
         
        This function reads a FCDC buffer header from a binary file or text file  
         
        On return, nameFlag has one of the following values:  
          0 = No labels were generated (fMRI etc.)  
          1 = Fake labels were generated  
          2 = Got channel labels from chunk information  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_buffer_offline_header.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_buffer_offline_header", *args, **kwargs)

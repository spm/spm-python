from spm._runtime import Runtime


def _read_buffer_offline_data(*args, **kwargs):
    r"""
      function dat = read_buffer_offline_data(datafile, header, range)  
         
        This function reads FCDC buffer-type data from a binary file.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_buffer_offline_data.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_buffer_offline_data", *args, **kwargs)

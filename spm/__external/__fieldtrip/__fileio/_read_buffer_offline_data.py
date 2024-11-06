from spm.__wrapper__ import Runtime


def _read_buffer_offline_data(*args, **kwargs):
    """
      function dat = read_buffer_offline_data(datafile, header, range)  
         
        This function reads FCDC buffer-type data from a binary file.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_buffer_offline_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_buffer_offline_data", *args, **kwargs)

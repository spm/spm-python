from spm.__wrapper__ import Runtime


def _read_spike6mat_header(*args, **kwargs):
    """
      read_spike6mat_header() - read Matlab files exported from Spike 6  
         
        Usage:  
          >> header = read_spike6mat_header(filename);  
         
        Inputs:  
          filename - [string] file name  
         
        Outputs:  
          header   - FILEIO toolbox type structure  
        _______________________________________________________________________  
        Copyright (C) 2008 Institute of Neurology, UCL  
        Vladimir Litvak  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_spike6mat_header.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_spike6mat_header", *args, **kwargs)

from spm.__wrapper__ import Runtime


def _read_spike6mat_data(*args, **kwargs):
    """
      read_spike6mat_data() - read Matlab files exported from Spike 6  
         
        Usage:  
          >> header = read_spike6mat_data(filename, varargin);  
         
        Inputs:  
          filename - [string] file name  
         
        Optional inputs:  
          'begsample'      first sample to read  
          'endsample'      last sample to read  
          'chanindx'  -    list with channel indices to read  
          'header'    - FILEIO structure header  
         
        Outputs:  
          dat    - data over the specified range  
        _______________________________________________________________________  
        Copyright (C) 2008 Institute of Neurology, UCL  
        Vladimir Litvak  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_spike6mat_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_spike6mat_data", *args, **kwargs)

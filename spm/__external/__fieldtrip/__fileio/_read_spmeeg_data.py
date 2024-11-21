from spm.__wrapper__ import Runtime


def _read_spmeeg_data(*args, **kwargs):
    """
      read_spmeeg_data() - import SPM5 and SPM8 meeg datasets  
         
        Usage:  
          >> header = read_spmeeg_data(filename, varargin);  
         
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
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
        Vladimir Litvak  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_spmeeg_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_spmeeg_data", *args, **kwargs)

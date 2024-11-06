from spm.__wrapper__ import Runtime


def _read_ah5_data(*args, **kwargs):
    """
    read_ah5_data is a function.  
          [data] = read_ah5_data(filename, hdr, begsample, endsample, chanindx)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ah5_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ah5_data", *args, **kwargs)

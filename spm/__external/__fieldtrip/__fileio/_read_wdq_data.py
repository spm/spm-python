from spm._runtime import Runtime


def _read_wdq_data(*args, **kwargs):
    """
      READ_WDQ_DATA reads data from wdq files  
         
        Use as  
         [dat] = read_wdq_data(filename, hdr, begsample, endsample, chanindx)  
        or  
         [dat] = read_wdq_data(filename, hdr, 'lowbits')  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_wdq_data.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_wdq_data", *args, **kwargs)

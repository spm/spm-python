from spm.__wrapper__ import Runtime


def _read_nex5_event(*args, **kwargs):
    """
      READ_NEX5_EVENT for Nex Technologies *.nex5 file, supports NEX5 variable types:  
          marker, interval, and event  
         
        Use as  
          [event] = read_nex5_event(filename)  
         
        The event.type used to select events in ft_trialfun_general is the  
        variable name from the NEX file (hdr.varheader.name - not to be confused  
        with hdr.varheader.type).  
         
        The sample numbers returned in event.sample correspond with the  
        timestamps, correcting for the difference in sampling frequency in the  
        continuous LFP channels and the system sampling frequency. Assuming 40kHz  
        sampling frequency for the system and 1kHz for the LFP channels, it is  
          event.sample = timestamp / (40000/1000);  
        If there are no continuous variables in the file, the system sampling  
        frequency is used throughout, so  
          event.sample = timestamp;  
         
        See also READ_NEX5_HEADER, READ_NEX5  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nex5_event.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_nex5_event", *args, **kwargs)

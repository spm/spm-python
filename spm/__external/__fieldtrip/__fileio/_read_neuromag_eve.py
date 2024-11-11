from spm.__wrapper__ import Runtime


def _read_neuromag_eve(*args, **kwargs):
    """
      READ_NEUROMAG_EVE imports events from the *.eve marker file that can accompany a  
        *.fif dataset.  
         
        Use as  
         [smp, tim, val3, val4] = read_neuromag_eve(filename)  
         
        Column one is the sample number. Column two is the time. Column three is is most  
        cases always zero, but is useful when you need to mark a segment rather than a  
        time point. Column four value is the event type you assign, i.e. the value of  
        the trigger.  
         
        The recording of the data to disk may start later than the actual data  
        acquisition. This is represented in hdr.orig.raw.first_samp. This potential  
        offset needs to be taken into acocunt when combining it with the data from the  
        file on disk.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuromag_eve.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuromag_eve", *args, **kwargs)

from spm.__wrapper__ import Runtime


def _read_trigger(*args, **kwargs):
    """
      READ_TRIGGER extracts the events from a continuous trigger channel  
        This function is a helper function to read_event and can be used for all  
        dataformats that have one or multiple continuously sampled TTL channels  
        in the data.  
         
        This is a helper function for FT_READ_EVENT. Please look at the code of  
        this function for further details.  
         
        TODO  
         - merge read_ctf_trigger into this function (requires trigshift and bitmasking option)  
         - merge biosemi code into this function (requires bitmasking option)  
         
        See also FT_READ_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_trigger.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_trigger", *args, **kwargs)

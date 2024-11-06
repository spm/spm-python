from spm.__wrapper__ import Runtime


def ft_write_event(*args, **kwargs):
    """
      FT_WRITE_EVENT writes an event structure to a file, a message daemon listening on a  
        network socked, or to another computer connected through the serial port. Note that  
        this function is mostly for real-time streaming of events. For most data files on  
        disk the writing of events is done simultaneously with the header and data in  
        FT_WRITE_DATA.  
         
        Use as  
          ft_write_event(filename, event, ...)  
         
        The first argument is a string containing the filename. The second argument is a  
        structure with the event. Multiple events can be represented as a structure array.  
        Events are represented in the same format as those returned by FT_READ_EVENT.  
          event.type      = string  
          event.sample    = expressed in samples, the first sample of a recording is 1  
          event.value     = number or string  
          event.offset    = expressed in samples  
          event.duration  = expressed in samples  
          event.timestamp = expressed in timestamp units, which vary over systems (optional)  
         
        Additional options should be specified in key-value pairs and can be  
          'eventformat'  = string, see below  
          'append'       = boolean, not supported for all formats  
         
        Events can be written to special communication streams by specifying the target as  
        URI instead of a filename. Supported are  
          buffer://<host>:<port>  
          fifo://<filename>  
          tcp://<host>:<port>  
          udp://<host>:<port>  
          mysql://<user>:<password>@<host>:<port>  
          rfb://<password>@<host>:<port>  
          serial:<port>?key1=value1&key2=value2&...  
          rfb://<password>@<host>:<port>  
         
        See also FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT, FT_WRITE_DATA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_write_event.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_write_event", *args, **kwargs, nargout=0)

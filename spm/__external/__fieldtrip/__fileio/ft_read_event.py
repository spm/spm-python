from spm.__wrapper__ import Runtime


def ft_read_event(*args, **kwargs):
    """
      FT_READ_EVENT reads all events from an EEG, MEG or other time series dataset and  
        returns them in a common data-independent structure. The supported formats are  
        listed in the accompanying FT_READ_HEADER function.  
         
        Use as  
          [event] = ft_read_event(filename, ...)  
         
        Additional options should be specified in key-value pairs and can be  
          'dataformat'     = string  
          'headerformat'   = string  
          'eventformat'    = string  
          'header'         = header structure, see FT_READ_HEADER  
          'detectflank'    = string, can be 'up', 'updiff', 'down', 'downdiff', 'both', 'any', 'biton', 'bitoff' (default is system specific)  
          'trigshift'      = integer, number of samples to shift from flank to detect trigger value (default = 0)  
          'chanindx'       = list with channel numbers for trigger detection, specify -1 in case you don't want to detect triggers (default is automatic)  
          'threshold'      = threshold for analog trigger channels (default is system specific)  
          'tolerance'      = tolerance in samples when merging Neuromag analogue trigger channels (default = 1, meaning that a shift of one sample in both directions is compensated for)  
          'blocking'       = wait for the selected number of events (default = 'no')  
          'timeout'        = amount of time in seconds to wait when blocking (default = 5)  
          'password'       = password structure for encrypted data set (only for dhn_med10, mayo_mef30 and mayo_mef21)  
          'readbids'       = 'yes', no', or 'ifmakessense', whether to read information from the BIDS sidecar files (default = 'ifmakessense')  
         
        This function returns an event structure with the following fields  
          event.type      = string  
          event.sample    = expressed in samples, the first sample of a recording is 1  
          event.value     = number or string  
          event.offset    = expressed in samples  
          event.duration  = expressed in samples  
          event.timestamp = expressed in timestamp units, which vary over systems (optional)  
         
        You can specify optional arguments as key-value pairs for filtering the events,  
        e.g. to select only events of a specific type, of a specific value, or events  
        between a specific begin and end sample. This event filtering is especially usefull  
        for real-time processing. See FT_FILTER_EVENT for more details.  
         
        Some data formats have trigger channels that are sampled continuously with the same  
        rate as the electrophysiological data. The default is to detect only the up-going  
        TTL flanks. The trigger events will correspond with the first sample where the TTL  
        value is up. This behavior can be changed using the 'detectflank' option, which  
        also allows for detecting the down-going flank or both. In case of detecting the  
        down-going flank, the sample number of the event will correspond with the first  
        sample at which the TTF went down, and the value will correspond to the TTL value  
        just prior to going down.  
         
        To use an external reading function, you can specify an external function as the  
        'eventformat' option. This function should take the filename  and the headeras  
        input arguments. Please check the code of this function for details, and search for  
        BIDS_TSV as example.  
         
        The event type and sample fields are always defined, other fields are present but  
        can be empty, depending on the type of event file. Events are sorted by the sample  
        on which they occur. After reading the event structure, you can use the following  
        tricks to extract information about those events in which you are interested.  
         
        Determine the different event types  
          unique({event.type})  
         
        Get the index of all trial events  
          find(strcmp('trial', {event.type}))  
         
        Make a vector with all triggers that occurred on the backpanel  
          [event(find(strcmp('backpanel trigger', {event.type}))).value]  
         
        Find the events that occurred in trial 26  
          t=26; samples_trials = [event(find(strcmp('trial', {event.type}))).sample];  
          find([event.sample]>samples_trials(t) & [event.sample]<samples_trials(t+1))  
         
        The list of supported file formats can be found in FT_READ_HEADER.  
         
        See also FT_READ_HEADER, FT_READ_DATA, FT_WRITE_EVENT, FT_FILTER_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_read_event.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_read_event", *args, **kwargs)

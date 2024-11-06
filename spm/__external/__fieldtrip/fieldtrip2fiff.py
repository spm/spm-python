from spm.__wrapper__ import Runtime


def fieldtrip2fiff(*args, **kwargs):
    """
      FIELDTRIP2FIFF saves a FieldTrip raw data structure as a fiff-file, allowing it  
        to be further analyzed by the Neuromag/Elekta/Megin software, or in MNE-python.  
         
        Use as  
          fieldtrip2fiff(filename, data)  
        where filename is the name of the output file, and data is a raw data structure  
        as obtained from FT_PREPROCESSING, or a timelock structure obtained from  
        FT_TIMELOCKANALYSIS. If the input data is a raw data structure with a single  
        trial, a continuous fif-file will be written. If the input data contains multiple  
        trials, either in a timelock or raw format, and epoched fif-file will be written.   
        If trials have different time axes, nans will be added to pad the trials to equal  
        length and time axis. If the input data contains an average across trials, an evoked  
        fif-file will be written.  
         
        Additional options can be specified as key-value pairs:  
          precision = string ('single'/'double'), determines the precision with which the  
                      numeric data is written to file, default is the class of the data.  
          coordsys  = string ('native'/'neuromag'), determines the coordinate system in which  
                      the MEG sensors are written (default = 'neuromag'). In case of   
                      'neuromag' the MEG sensors are expressed in (approximate) neuromag  
                      coordinates, which may facilitate downstream handling of the fif-files  
                      in other software such as MNE-python. This is according to the  
                      official fif-file format definition. This option does not have an  
                      effect on EEG electrodes or fNIRS optodes.  
          event     = structure as obtained from FT_READ_EVENT, note that the sampling in the  
                      event structure should be the same as the sampling of the data structure,  
                      i.e. the values in data.sampleinfo should be in line with event.sample, and  
                      the sampling rate should be the same. No check will be performed. Also, the   
                      events will only be written to file if the input data is of type raw with  
                      a single trial.                 
          eventtype = string or cell array of string with the event types to be  
                      written to the continuous fif-file (default is all)  
          hdr       = structure as obtained from FT_READ_HEADER  
          
        If present in the data, the original header is reused (also removing the non-used channels).  
        Otherwise, the function attempts to create the header, which might or might not be correct  
        (e.g. with respect to the scaling and the sensor locations).   
          
        The events are written in MNE format (three columns) into the continuous  
        fif-file, with a mapping string that allows for a richer interpretation of the events.  
          
        See also FT_DATATYPE_RAW, FT_DATATYPE_TIMELOCK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fieldtrip2fiff.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fieldtrip2fiff", *args, **kwargs, nargout=0)

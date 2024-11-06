from spm.__wrapper__ import Runtime


def xdf2fieldtrip(*args, **kwargs):
    """
      XDF2FIELDTRIP reads continuously sampled data from a XDF file with multiple  
        streams. It upsamples the data of all streams to the highest sampling rate and  
        concatenates all channels in all streams into a raw data structure that is  
        compatible with the output of FT_PREPROCESSING.  
         
        Use as  
          [data, events] = xdf2fieldtrip(filename, ...)  
         
        Optional arguments should come in key-value pairs and can include  
          streamindx      = number or list, indices of the streams to read (default is all)  
          streamrate      = [lowerbound upperbound], read only data streams within this range of sampling rates (in Hz)  
          streamkeywords  = cell-array with strings, keywords contained in the stream to read  
         
        You can also use the standard procedure with FT_DEFINETRIAL and FT_PREPROCESSING  
        for XDF files. This will return (only) the continuously sampled stream with the  
        highest sampling rate, which is typically the EEG.  
         
        You can also use FT_READ_EVENT to read the events from the non-continuous data  
        streams. To get them aligned with the samples in one of the specific data streams,  
        you should specify the corresponding header structure.  
         
        See also FT_PREPROCESSING, FT_DEFINETRIAL, FT_REDEFINETRIAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/xdf2fieldtrip.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("xdf2fieldtrip", *args, **kwargs)

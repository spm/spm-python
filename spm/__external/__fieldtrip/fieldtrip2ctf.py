from spm.__wrapper__ import Runtime


def fieldtrip2ctf(*args, **kwargs):
    """
      FIELDTRIP2CTF saves a FieldTrip data structure to a CTF dataset.  
         
        The file to which the data is exported depends on the input data structure that you  
        provide. The "raw" and "timelock" structures can be exported to a CTF dataset. The  
        "montage" structure can be exported to a CTF "Virtual Channels" file.  
         
        Use as  
          fieldtrip2ctf(filename, data, ...)  
        where filename is a string and data is a FieldTrip raw, timelock or montage  
        structure.  
         
        Additional options should be specified in key-value pairs and can be  
          'ds' = struct, original dataset information as obtained with readCTFds  
         
        See also FT_DATATYPE, FT_APPLY_MONTAGE, FT_VOLUMEWRITE, FT_SOURCEWRITE, FT_WRITE_DATA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fieldtrip2ctf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fieldtrip2ctf", *args, **kwargs, nargout=0)

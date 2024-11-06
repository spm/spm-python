from spm.__wrapper__ import Runtime


def ft_datatype(*args, **kwargs):
    """
      FT_DATATYPE determines the type of data represented in a FieldTrip data structure  
        and returns a string with raw, freq, timelock source, comp, spike, source, volume,  
        dip, montage, event.  
         
        Use as  
          [type, dimord] = ft_datatype(data)  
          [bool]         = ft_datatype(data, desired)  
         
        See also FT_DATATYPE_COMP, FT_DATATYPE_FREQ, FT_DATATYPE_MVAR,  
        FT_DATATYPE_SEGMENTATION, FT_DATATYPE_PARCELLATION, FT_DATATYPE_SOURCE,  
        FT_DATATYPE_TIMELOCK, FT_DATATYPE_DIP, FT_DATATYPE_HEADMODEL,  
        FT_DATATYPE_RAW, FT_DATATYPE_SENS, FT_DATATYPE_SPIKE, FT_DATATYPE_VOLUME  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_datatype.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_datatype", *args, **kwargs)

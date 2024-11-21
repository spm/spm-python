from spm.__wrapper__ import Runtime


def ft_warning(*args, **kwargs):
    """
      FT_WARNING prints a warning message on screen, depending on the verbosity   
        settings of the calling high-level FieldTrip function. This function works  
        similar to the standard WARNING function, but also features the "once" mode.  
         
        Use as  
          ft_warning(...)  
        with arguments similar to fprintf, or  
          ft_warning(msgId, ...)  
        with arguments similar to warning.  
         
        You can switch of all warning messages using  
          ft_warning off  
        or for specific ones using  
          ft_warning off msgId  
         
        To switch them back on, you would use   
          ft_warning on  
        or for specific ones using  
          ft_warning on msgId  
          
        Warning messages are only printed once per timeout period using  
          ft_warning timeout 60  
          ft_warning once  
        or for specific ones using  
          ft_warning once msgId  
         
        You can see the most recent messages and identifier using  
          ft_warning last  
         
        You can query the current on/off/once state for all messages using  
          ft_warning query  
         
        See also FT_ERROR, FT_WARNING, FT_NOTICE, FT_INFO, FT_DEBUG, ERROR, WARNING  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_warning.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_warning", *args, **kwargs)

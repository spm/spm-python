from spm.__wrapper__ import Runtime


def _ft_notice(*args, **kwargs):
    """
      FT_NOTICE prints a notice message on screen, depending on the verbosity   
        settings of the calling high-level FieldTrip function.  
         
        Use as  
          ft_notice(...)  
        with arguments similar to fprintf, or  
          ft_notice(msgId, ...)  
        with arguments similar to warning.  
         
        You can switch of all messages using  
          ft_notice off  
        or for specific ones using  
          ft_notice off msgId  
         
        To switch them back on, you would use   
          ft_notice on  
        or for specific ones using  
          ft_notice on msgId  
          
        Messages are only printed once per timeout period using  
          ft_notice timeout 60  
          ft_notice once  
        or for specific ones using  
          ft_notice once msgId  
         
        You can see the most recent messages and identifier using  
          ft_notice last  
         
        You can query the current on/off/once state for all messages using  
          ft_notice query  
         
        See also FT_ERROR, FT_WARNING, FT_NOTICE, FT_INFO, FT_DEBUG, ERROR, WARNING  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/ft_notice.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_notice", *args, **kwargs)

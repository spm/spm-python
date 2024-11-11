from spm.__wrapper__ import Runtime


def _ft_notification(*args, **kwargs):
    """
      FT_NOTIFICATION works mostly like the WARNING and ERROR commands in MATLAB and  
        is called by FT_ERROR, FT_WARNING, FT_NOTICE, FT_INFO and FT_DEBUG. Please note  
        that you should not call this function directly.  
         
        Some examples:  
         ft_info on  
         ft_info on msgId  
         ft_info off  
         ft_info off msgId  
         ft_info once  
         ft_info once msgId  
         ft_info on  backtrace  
         ft_info off backtrace  
         ft_info on  verbose  
         ft_info off verbose  
         
         ft_info query      % shows the status of all notifications  
         ft_info last       % shows the last notification  
         ft_info clear      % clears the status of all notifications  
         ft_info timeout 10 % sets the timeout (for 'once') to 10 seconds  
         
        See also DEFAULTID, FT_ERROR, FT_WARNING, FT_NOTICE, FT_INFO, FT_DEBUG, ERROR, WARNING  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/ft_notification.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_notification", *args, **kwargs)

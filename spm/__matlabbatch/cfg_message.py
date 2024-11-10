from spm.__wrapper__ import Runtime


def cfg_message(*args, **kwargs):
    """
      function cfg_message(msgid, msgfmt, varargin)  
        Display a message. The message identifier msgid will be looked up in a  
        message database to decide how to treat this message. This database is  
        a struct array with fields:  
        .identifier  - message id  
        .level       - message severity level. One of  
                       'info'    - print message  
                       'warning' - print message, raise a warning  
                       'error'   - print message, throw an error  
        .destination - output destination. One of  
                       'none'    - silently ignore this message  
                       'stdout'  - standard output  
                       'stderr'  - standard error output  
                       'syslog'  - (UNIX) syslog  
                       Warnings and errors will always be logged to the command  
                       window and to syslog, if destination == 'syslog'. All  
                       other messages will only be logged to the specified location.  
        .verbose  
        .backtrace   - control verbosity and backtrace, one of 'on' or 'off'  
         
        function [oldsts msgids] = cfg_message('on'|'off', 'verbose'|'backtrace', msgidregexp)  
        Set verbosity and backtrace display for all messages where msgid  
        matches msgidregexp. To match a message id exactly, use the regexp  
        '^msgid$'.  
         
        function [olddest msgids] = cfg_message('none'|'stdout'|'stderr'|'syslog', 'destination', msgidregexp)  
        Set destination for all messages matching msgidregexp.  
         
        function [oldlvl msgids] = cfg_message('info'|'warning'|'error', 'level', msgidregexp)  
        Set severity level for all messages matching msgidregexp.  
         
        For all matching message ids and message templates, the old value and  
        the id are returned as cell strings. These can be used to restore  
        previous settings one-by-one.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_message.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_message", *args, **kwargs)

from spm.__wrapper__ import Runtime


def _ft_progress(*args, **kwargs):
    """
      FT_PROGRESS shows a graphical or non-graphical progress indication similar to the  
        standard WAITBAR function, but with the extra option of printing it in the command  
        window as a plain text string or as a rotating dial. Alternatively, you can also  
        specify it not to give feedback on the progress.  
         
        Prior to the for-loop, you should call either  
          ft_progress('init', 'none',    'Please wait...')  
          ft_progress('init', 'text',    'Please wait...')  
          ft_progress('init', 'textbar', 'Please wait...')      % ascii progress bar  
          ft_progress('init', 'dial',    'Please wait...')      % rotating dial  
          ft_progress('init', 'etf',     'Please wait...')      % estimated time to finish  
          ft_progress('init', 'gui',     'Please wait...')  
         
        In each iteration of the for-loop, you should call either  
        ft_progress(x)                                          % only show percentage  
        ft_progress(x, 'Processing event %d from %d', i, N)     % show string, x=i/N  
         
        After finishing the for-loop, you should call  
          ft_progress('close')  
         
        Here is an example for the use of a progress indicator  
          ft_progress('init', 'etf', 'Please wait...');  
          for i=1:100  
            ft_progress(i/100, 'Processing event %d from %d', i, 100);  
            pause(0.03);  
          end  
          ft_progress('close')  
         
        See also WAITBAR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/ft_progress.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_progress", *args, **kwargs, nargout=0)

from spm.__wrapper__ import Runtime


def ft_wizard(*args, **kwargs):
    """
      FT_WIZARD is a graphical user interface to evaluate a FieldTrip analysis  
        script one step at a time, allowing you to go to the next step if you are  
        content with the data so far, or to the previous step if you want to repeat it  
        with different configuration settings.  
         
        Use as  
          ft_wizard scriptname  
        or   
          ft_wizard('scriptname')  
         
        Use the functional form of FT_WIZARD, such as FT_WIZARD('scriptname'), when  
        the name of the script is stored in a string, when an output argument is  
        requested, or if the name of the script contains spaces. If you do not  
        specify an output argument, the results will be stored as variables in  
        the main MATLAB workspace.   
          
        Besides the buttons, you can use the following key combinations  
          Ctrl-O        load a new script from a file  
          Ctrl-S        save the script to a new file  
          Ctrl-E        open the current script in editor  
          Ctrl-P        go to previous step  
          Ctrl-N        go to next step  
          Ctrl-Q        quit, do not save the variables  
          Ctrl-X        exit, save the variables to the workspace  
          
        See also FT_ANALYSISPROTOCOL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_wizard.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_wizard", *args, **kwargs)

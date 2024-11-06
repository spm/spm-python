from spm.__wrapper__ import Runtime


def spm_progress_bar(*args, **kwargs):
    """
      Display a 'Progress Bar' in the 'Interactive' window  
        FORMAT spm_progress_bar('Init',height,xlabel,ylabel,flgs)  
        Initialise the bar in the 'Interactive' window.  
        If flgs contains a 't', then use tex interpreter for labels.  
         
        FORMAT spm_progress_bar('Set',value)  
        Set the height of the bar itself.  
         
        FORMAT spm_progress_bar('Set','xlabel',xlabel)  
        FORMAT spm_progress_bar('Set','ylabel',ylabel)  
        Set the progress bar labels.  
         
        FORMAT spm_progress_bar('Set','height',height)  
        Set the height of the progress bar.  
         
        FORMAT spm_progress_bar('Clear')  
        Clear the 'Interactive' window.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_progress_bar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_progress_bar", *args, **kwargs, nargout=0)

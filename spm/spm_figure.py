from spm.__wrapper__ import Runtime


def spm_figure(*args, **kwargs):
    """
      Setup and callback functions for Graphics window  
        FORMAT varargout = spm_figure(varargin)  
         
        spm_figure provides utility routines for using the SPM Graphics  
        interface. Most used syntaxes are listed here, see the embedded callback  
        reference in the main body of this function, below the help text.  
         
        FORMAT F = spm_figure('Create',Tag,Name,Visible)  
        FORMAT F = spm_figure('FindWin',Tag)  
        FORMAT F = spm_figure('GetWin',Tag)  
        FORMAT spm_figure('Select',F)  
        FORMAT spm_figure('Focus',F)  
        FORMAT spm_figure('Clear',F,Tags)  
        FORMAT spm_figure('Close',F)  
        FORMAT spm_figure('Print',F)  
        FORMAT spm_figure('WaterMark',F,str,Tag,Angle,Perm)  
         
        FORMAT spm_figure('NewPage',hPage)  
        FORMAT spm_figure('TurnPage',move,F)  
        FORMAT spm_figure('DeletePageControls',F)  
        FORMAT n = spm_figure('#page')  
        FORMAT n = spm_figure('CurrentPage')  
       __________________________________________________________________________  
         
        spm_figure creates and manages the 'Graphics' window. This window and  
        these facilities may be used independently of SPM, and any number of  
        Graphics windows my be used within the same MATLAB session. (Though  
        only one SPM 'Graphics' 'Tag'ed window is permitted).  
         
        The Graphics window is provided with a menu bar at the top that  
        facilitates editing and printing of the current graphic display.  
         
        "Print": Graphics windows with multi-page axes are printed page by page.  
         
        "Clear": Clears the Graphics window. If in SPM usage (figure 'Tag'ed as  
        'Graphics') then all SPM windows are cleared and reset.  
         
        "Colours": Sets or adjusts the colormap.  
         
        For SPM usage, the figure should be 'Tag'ed as 'Graphics'.  
         
        See also: spm_print, spm_clf, spm_colourmap  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_figure.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_figure", *args, **kwargs)

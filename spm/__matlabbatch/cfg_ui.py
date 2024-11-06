from spm.__wrapper__ import Runtime


def cfg_ui(*args, **kwargs):
    """
      CFG_UI M-File for cfg_ui.fig  
             CFG_UI, by itself, creates a new CFG_UI or raises the existing  
             singleton*.  
         
             H = CFG_UI returns the handle to a new CFG_UI or the handle to  
             the existing singleton*.  
         
             CFG_UI('CALLBACK',hObject,eventData,handles,...) calls the local  
             function named CALLBACK in CFG_UI.M with the given input arguments.  
         
             CFG_UI('Property','Value',...) creates a new CFG_UI or raises the  
             existing singleton*.  Starting from the left, property value pairs are  
             applied to the GUI before cfg_ui_OpeningFcn gets called.  An  
             unrecognized property name or invalid value makes property application  
             stop.  All inputs are passed to cfg_ui_OpeningFcn via varargin.  
         
             *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one  
             instance to run (singleton)".  
         
        See also: GUIDE, GUIDATA, GUIHANDLES  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_ui", *args, **kwargs)

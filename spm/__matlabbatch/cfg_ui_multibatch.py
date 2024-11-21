from spm.__wrapper__ import Runtime


def cfg_ui_multibatch(*args, **kwargs):
    """
      CFG_UI_MULTIBATCH MATLAB code for cfg_ui_multibatch.fig  
             CFG_UI_MULTIBATCH, by itself, creates a new CFG_UI_MULTIBATCH or raises the existing  
             singleton*.  
         
             H = CFG_UI_MULTIBATCH returns the handle to a new CFG_UI_MULTIBATCH or the handle to  
             the existing singleton*.  
         
             CFG_UI_MULTIBATCH('CALLBACK',hObject,eventData,handles,...) calls the local  
             function named CALLBACK in CFG_UI_MULTIBATCH.M with the given input arguments.  
         
             CFG_UI_MULTIBATCH('Property','Value',...) creates a new CFG_UI_MULTIBATCH or raises the  
             existing singleton*.  Starting from the left, property value pairs are  
             applied to the GUI before cfg_ui_multibatch_OpeningFcn gets called.  An  
             unrecognized property name or invalid value makes property application  
             stop.  All inputs are passed to cfg_ui_multibatch_OpeningFcn via varargin.  
         
             *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one  
             instance to run (singleton)".  
         
        See also: GUIDE, GUIDATA, GUIHANDLES  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_ui_multibatch.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_ui_multibatch", *args, **kwargs)

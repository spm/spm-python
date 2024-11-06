from spm.__wrapper__ import Runtime


def DEM_demo(*args, **kwargs):
    """
      DEM_DEMO M-file for DEM_demo.fig  
             DEM_DEMO, by itself, creates a new DEM_DEMO or raises the existing  
             singleton*.  
         
             H = DEM_DEMO returns the handle to a new DEM_DEMO or the handle to  
             the existing singleton*.  
         
             DEM_DEMO('CALLBACK',hObject,eventData,handles,...) calls the local  
             function named CALLBACK in DEM_DEMO.M with the given input arguments.  
         
             DEM_DEMO('Property','Value',...) creates a new DEM_DEMO or raises the  
             existing singleton*.  Starting from the left, property value pairs are  
             applied to the GUI before DEM_demo_OpeningFunction gets called.  An  
             unrecognized property name or invalid value makes property application  
             stop.  All inputs are passed to DEM_demo_OpeningFcn via varargin.  
         
             *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one  
             instance to run (singleton)".  
         
        See also: GUIDE, GUIDATA, GUIHANDLES  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo", *args, **kwargs)

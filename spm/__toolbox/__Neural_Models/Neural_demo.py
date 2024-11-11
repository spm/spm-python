from spm.__wrapper__ import Runtime


def Neural_demo(*args, **kwargs):
    """
      NEURAL_DEMO M-file for Neural_demo.fig  
             NEURAL_DEMO, by itself, creates a new NEURAL_DEMO or raises the existing  
             singleton*.  
         
             H = NEURAL_DEMO returns the handle to a new NEURAL_DEMO or the handle to  
             the existing singleton*.  
         
             NEURAL_DEMO('CALLBACK',hObject,eventData,handles,...) calls the local  
             function named CALLBACK in NEURAL_DEMO.M with the given input arguments.  
         
             NEURAL_DEMO('Property','Value',...) creates a new NEURAL_DEMO or raises the  
             existing singleton*.  Starting from the left, property value pairs are  
             applied to the GUI before Neural_demo_OpeningFunction gets called.  An  
             unrecognized property name or invalid value makes property application  
             stop.  All inputs are passed to Neural_demo_OpeningFcn via varargin.  
         
             *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one  
             instance to run (singleton)".  
         
        See also: GUIDE, GUIDATA, GUIHANDLES  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/Neural_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("Neural_demo", *args, **kwargs)

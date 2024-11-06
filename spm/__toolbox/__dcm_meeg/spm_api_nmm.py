from spm.__wrapper__ import Runtime


def spm_api_nmm(*args, **kwargs):
    """
      SPM_API_NMM M-file for spm_api_nmm.fig  
             SPM_API_NMM, by itself, creates a new SPM_API_NMM or raises the existing  
             singleton*.  
         
             H = SPM_API_NMM returns the handle to a new SPM_API_NMM or the handle to  
             the existing singleton*.  
         
             SPM_API_NMM('CALLBACK',hObject,eventData,handles,...) calls the local  
             function named CALLBACK in SPM_API_NMM.M with the given input arguments.  
         
             SPM_API_NMM('Property','Value',...) creates a new SPM_API_NMM or raises the  
             existing singleton*.  Starting from the left, property value pairs are  
             applied to the GUI before spm_api_nmm_OpeningFunction gets called.  An  
             unrecognized property name or invalid value makes property application  
             stop.  All inputs are passed to spm_api_nmm_OpeningFcn via varargin.  
         
             *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one  
             instance to run (singleton)".  
         
        See also: GUIDE, GUIDATA, GUIHANDLES  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_api_nmm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_api_nmm", *args, **kwargs)

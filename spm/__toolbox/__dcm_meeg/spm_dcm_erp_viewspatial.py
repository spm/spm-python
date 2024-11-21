from spm.__wrapper__ import Runtime


def spm_dcm_erp_viewspatial(*args, **kwargs):
    """
      SPM_DCM_ERP_VIEWSPATIAL M-file for spm_dcm_erp_viewspatial.fig  
             SPM_DCM_ERP_VIEWSPATIAL, by itself, creates a new SPM_DCM_ERP_VIEWSPATIAL or raises the existing  
             singleton*.  
         
             H = SPM_DCM_ERP_VIEWSPATIAL returns the handle to a new SPM_DCM_ERP_VIEWSPATIAL or the handle to  
             the existing singleton*.  
         
             SPM_DCM_ERP_VIEWSPATIAL('CALLBACK',hObject,eventData,handles,...) calls the local  
             function named CALLBACK in SPM_DCM_ERP_VIEWSPATIAL.M with the given input arguments.  
         
             SPM_DCM_ERP_VIEWSPATIAL('Property','Value',...) creates a new SPM_DCM_ERP_VIEWSPATIAL or raises the  
             existing singleton*.  Starting from the left, property value pairs are  
             applied to the GUI before spm_dcm_erp_viewspatial_OpeningFunction gets called.  An  
             unrecognized property name or invalid value makes property application  
             stop.  All inputs are passed to spm_dcm_erp_viewspatial_OpeningFcn via varargin.  
         
             *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one  
             instance to run (singleton)".  
         
        See also: GUIDE, GUIDATA, GUIHANDLES  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_erp_viewspatial.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_erp_viewspatial", *args, **kwargs)

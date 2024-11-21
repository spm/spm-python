from spm.__wrapper__ import Runtime


def spm_COVID_Y(*args, **kwargs):
    """
      prepares data array for COVID routines  
        FORMAT [Y,S,dates] = spm_COVID_Y(Y,date0)  
        Y     - structure array  
        date0 - initial date ('dd-mm-yyy')  
        days  - number of days over which to average (smooth)  
         
        Y     - structure array (time ordered, withough NaNs and smoothed)  
        S     - corresponding data matrix  
        dates - date numbers from 'dd-mm-yyyy' to last data point  
         
           Y(i).type = datatype (string)  
           Y(i).unit = units (string)  
           Y(i).U    = output index (from spm_SARS_gen);  
           Y(i).date = date number of data points;  
           Y(i).Y    = data points (vector)  
           Y(i).h    = log-precision  
           Y(i).n    = number of data points  
           Y(i).s    = smoothing (days)  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_Y.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_COVID_Y", *args, **kwargs)

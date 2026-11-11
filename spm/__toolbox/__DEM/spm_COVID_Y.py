from spm._runtime import Runtime


def spm_COVID_Y(*args, **kwargs):
    r"""
      prepares data array for COVID routines  
        FORMAT [Y,S,dates] = spm_COVID_Y(Y,date0)  
        Y     - structure array  
        date0 - initial date ('dd-mmm-yyyy')  
        days  - number of days over which to average (smooth)  
        date1 - final date ('dd-mmm-yyyy') [default: date]  
         
        Y     - structure array (time ordered, withough NaNs and smoothed)  
        S     - corresponding data matrix  
        dates - date numbers from 'dd-mmm-yyyy' to last data point  
         
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_COVID_Y.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_COVID_Y", *args, **kwargs)

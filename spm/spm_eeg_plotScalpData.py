from spm._runtime import Runtime


def spm_eeg_plotScalpData(*args, **kwargs):
    r"""
      Display M/EEG interpolated sensor data on a scalp image  
        FORMAT [ZI,f] = spm_eeg_plotScalpData(Z,pos,ChanLabel,in)  
         
        INPUT:  
          Z          - the data matrix at the sensors  
          pos        - the positions of the sensors  
          ChanLabel  - the names of the sensors  
          in         - a structure containing some information related to the   
                       main PRESELECTDATA window. This entry is not necessary  
        OUTPUT:  
          ZI         - an image of interpolated data onto the scalp  
          f          - the handle of the figure which displays the interpolated  
                       data  
       __________________________________________________________________________  
         
        This function creates a figure whose purpose is to display an  
        interpolation of the sensor data on the scalp (as an image).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_plotScalpData.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_plotScalpData", *args, **kwargs)

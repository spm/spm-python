from spm.__wrapper__ import Runtime


def spm_eeg_plotScalpData(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_plotScalpData.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_plotScalpData", *args, **kwargs)

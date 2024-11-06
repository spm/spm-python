from spm.__wrapper__ import Runtime


def _opto2homer(*args, **kwargs):
    """
      OPTO2HOMER constructs a Homer-compatible sensor definition (SD) from a FieldTrip  
        opto structure.  
         
        See https://www.nitrc.org/plugins/mwiki/index.php/homer2:Homer_Input_Files#NIRS_data_file_format  
         
        The Homer SD structure contains the source/detector geometry and has the following fields:  
         
        nSrcs    - Number of lasers; scalar variable  
        nDets    - Number of detectors; scalar variable  
        SrcPos   - Array of probe coordinates of the lasers; dimensions <number of lasers> by 3  
        DetPos   - Array of probe coordinates of the detectors; dimensions <number of detectors> by 3  
        Lambda   - Wavelengths used for data acquisition; dimensions <number of wavelengths> by 1  
        MeasList - List of source/detector/wavelength measurement channels. It’s an array with dimensions, <number of channels> by 4.The meaning of the 4 columns are as follows:  
          Column 1 index of the source from the SD.SrcPos list.  
          Column 2 index of the detector from the SD.DetPos list.  
          Column 3 is unused right now and contains all ones.  
          Column 4 index of the wavelength from SD.Lambda.  
         
        The FieldTrip optode structure is defined in FT_DATATYPE_SENS  
         
        See also HOMER2OPTO, FT_DATATYPE_SENS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/opto2homer.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("opto2homer", *args, **kwargs)

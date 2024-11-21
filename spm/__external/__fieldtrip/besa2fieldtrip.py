from spm.__wrapper__ import Runtime


def besa2fieldtrip(*args, **kwargs):
    """
      BESA2FIELDTRIP reads and converts various BESA datafiles into a FieldTrip  
        data structure, which subsequently can be used for statistical analysis  
        or other analysis methods implemented in Fieldtrip.  
         
        Use as  
          [output] = besa2fieldtrip(input)  
        where the input should be a string specifying the BESA file, or a MATLAB structure  
        with data that was exported by BESA. The output is a MATLAB structure that is  
        compatible with FieldTrip.  
         
        The format of the output structure depends on the type of datafile:  
          *.avr is converted to a structure similar to the output of FT_TIMELOCKANALYSIS  
          *.mul is converted to a structure similar to the output of FT_TIMELOCKANALYSIS  
          *.swf is converted to a structure similar to the output of FT_TIMELOCKANALYSIS (*)  
          *.tfc is converted to a structure similar to the output of FT_FREQANALYSIS     (*)  
          *.dat is converted to a structure similar to the output of FT_SOURCANALYSIS  
          *.dat combined with a *.gen or *.generic is converted to a structure similar to the output of FT_PREPROCESSING  
         
        (*) If the BESA toolbox by Karsten Hochstatter is found on your MATLAB path, the  
        readBESAxxx functions will be used (where xxx=tfc/swf), alternatively the private  
        functions from FieldTrip will be used.  
         
        See also EEGLAB2FIELDTRIP, SPM2FIELDTRIP  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/besa2fieldtrip.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("besa2fieldtrip", *args, **kwargs)

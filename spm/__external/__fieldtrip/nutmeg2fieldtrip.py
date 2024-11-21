from spm.__wrapper__ import Runtime


def nutmeg2fieldtrip(*args, **kwargs):
    """
      NUTMEG2FIELDTRIP converts from NUTMEG either a sensor data structure  
        ('nuts') to a valid FieldTrip 'raw' structure (plus 'sourcemodel' and  
        'mri' if available), OR a source structure ('beam') to a valid FieldTrip  
        source structure.  
         
        Use as  
           [data, mri, sourcemodel] = nutmeg2fieldtrip(cfg, fileorstruct)  
         
        Input:  
             cfg  
                 .keepmri (required for either input): =1 calls ft_read_mri for 'mri' output; =0 not save out 'mri'  
                 .out     (required for source input): 's' (pos_freq_time) or 'trial' (pos_rpt)  
             fileorstruct: may be one of following:  
                1) *.mat file containing nuts sensor structure  
                2) nuts sensor structure  
                3) s*.mat file containing beam source structure  
                4) beam source structure (output from Nutmeg (beamforming_gui, tfbf, or tfZ)  
                      (only scalar not vector results supported at the moment)  
         
        Output: depending on input, one of options  
                1) If nuts sensor structure input, then 'data' will be 'raw' and  
                   optionally 'sourcemodel' if Lp present, or 'mri' if individual MRI present  
                2) If beam source structure input, then 'data' will be 'source'  
                   (May be an array of source structures (source{1} etc))  
                   'sourcemodel' and 'mri' may be output as well if present in beam structure  
         
        See alo FT_DATATYPE_RAW, FT_DATATYPE_SOURCE, LORETA2FIELDTRIP, SPASS2FIELDTRIP,  
        FIELDTRIP2SPSS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/nutmeg2fieldtrip.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("nutmeg2fieldtrip", *args, **kwargs)

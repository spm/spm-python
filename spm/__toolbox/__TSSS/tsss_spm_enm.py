from spm.__wrapper__ import Runtime


def tsss_spm_enm(*args, **kwargs):
    """
      Perform tSSS on rawdata file 'infile' acquired with an Elekta Neuromag  
        306-channel MEG system. The tSSS-processed data are written into 'outfile'.  
        The SSS operation is performed in the head coordinate system with the  
        expansion origin given by the 3x1 dimensional vector 'r_sphere' ([x y z]  
        m; typically [0 0 0.04]). The temporal correlation analysis of tSSS is based  
        on raw data segments of length 't_window' (in seconds) and correlation limit  
        'corr_limit'. The order values of the internal and external SSS bases are  
        'Lin' and 'Lout', typically 8 and 3, respectively.   
         
        NOTE: This tSSS function does not utilize the so-called fine calibration  
        information of the MEG system. Also, no basis vector selection is  
        performed as a regularization step. Ideally, the input file 'infile'  
        should contain cross-talk compensated data, which can be done by the  
        MaxFilter software.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/TSSS/tsss_spm_enm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tsss_spm_enm", *args, **kwargs)

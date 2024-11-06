from spm.__wrapper__ import Runtime


def spm_eeg_megheadloc(*args, **kwargs):
    """
      Use head localization of CTF to select/reject trials based on head  
        position and (optionally) correct the sensor coordinates to correspond to  
        the selected trials. The function can be used on a single dataset as well  
        as several datasets together. Most of the functionality requires the  
        original CTF header (read with CTF toolbox) to be present (set  
        S.saveorigheader = 1 at conversion).  
         
        FORMAT D = spm_eeg_megheadloc(S)  
         
        S         - struct (optional)  
        (optional) fields of S:  
        S.D - meeg object, filename or a list of filenames of SPM EEG files  
        S.rejectbetween - reject trials based on their difference from other  
                          trials (1 - yes, 0- no).  
        S.threshold -     distance threshold for rejection (in meters), default  
                          0.01 (1 cm)  
        S.rejectwithin -  reject trials based on excessive movement within trial  
        S.trialthresh -   distance threshold for rejection (in meters), default  
                          0.005 (0.5 cm)  
        S.losttrack   -   how to handle segments where the system lost track of  
                          one of the coils.  
                          'reject' - reject the trial  
                          'preserve' - try to preserve the trials. The exact  
                          behavior depends on 'rejectbetween' and 'rejectwithin'  
                          settings  
         
        S.correctsens -   calculate corrected sensor representation and put it in  
                          the dataset.  
        S.trialind    -   only look at a subset of trials specified. Can be used  
                          to work trial-by trial with a single file.  
        S.save        -   save the header files (otherwise just return the headers).  
        S.toplot      -   plot feedback information (default 1, yes).  
         
        Output:  
        D         - MEEG data struct or cell array of MEEG objects with the  
                    rejected trials set to bad and sensors corrected (if  
                    requested).  
         
        Disclaimer: this code is provided as an example and is not guaranteed to work  
        with data on which it was not tested. If it does not work for you, feel  
        free to improve it and contribute your improvements to the MEEGtools toolbox  
        in SPM (http://www.fil.ion.ucl.ac.uk/spm)  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_megheadloc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_megheadloc", *args, **kwargs)

from spm.__wrapper__ import Runtime


def spm(*args, **kwargs):
    """
      SPM: Statistical Parametric Mapping (startup function)  
       _______________________________________________________________________  
         ___  ____  __  __  
        / __)(  _ \(  \/  )    
        \__ \ )___/ )    (   Statistical Parametric Mapping  
        (___/(__)  (_/\/\_)  SPM - https://www.fil.ion.ucl.ac.uk/spm/  
       _______________________________________________________________________  
         
        SPM (Statistical Parametric Mapping) is a package for the analysis  
        functional brain mapping experiments. It is the in-house package of  
        the Wellcome Centre for Human Neuroimaging, and is available to the  
        scientific community as copyright freeware under the terms of the  
        GNU General Public Licence.  
          
        Theoretical, computational and other details of the package are  
        available in SPM's "Help" facility. This can be launched from the  
        main SPM Menu window using the "Help" button, or directly from the  
        command line using the command `spm_help`.  
         
        Details of this release are available via the "About SPM" help topic  
        accessible from the SPM splash screen. See also README.md.  
          
        This spm function initialises the default parameters, and displays a  
        splash screen with buttons leading to the PET, fMRI and M/EEG  
        modalities. Alternatively, `spm('pet')`, `spm('fmri')`, `spm('eeg')`  
        (equivalently `spm pet`, `spm fmri` and `spm eeg`) lead directly to   
        the respective modality interfaces.  
         
        Once the modality is chosen, (and it can be toggled mid-session) the  
        SPM user interface is displayed. This provides a constant visual  
        environment in which data analysis is implemented. The layout has  
        been designed to be simple and at the same time show all the  
        facilities that are available. The interface consists of three  
        windows: A menu window with pushbuttons for the SPM routines (each  
        button has a 'CallBack' string which launches the appropriate  
        function/script); A blank panel used for interaction with the user;  
        And a graphics figure with various editing and print facilities (see  
        spm_figure.m). (These windows are 'Tag'ged 'Menu', 'Interactive', and  
        'Graphics' respectively, and should be referred to by their tags  
        rather than their figure numbers.)  
         
        Further interaction with the user is (mainly) via questioning in the  
        'Interactive' window (managed by spm_input), and file selection  
        (managed by spm_select). See the help on spm_input.m and spm_select.m for  
        details on using these functions.  
         
        Arguments to this routine (spm.m) lead to various setup facilities,  
        mainly of use to SPM power users and programmers. See programmers  
        FORMAT & help in the main body of spm.m  
         
       _______________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm", *args, **kwargs)

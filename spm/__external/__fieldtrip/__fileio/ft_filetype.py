from spm.__wrapper__ import Runtime


def ft_filetype(*args, **kwargs):
    """
      FT_FILETYPE determines the filetype of many EEG/MEG/MRI data files by  
        looking at the name, extension and optionally (part of) its contents.  
        It tries to determine the global type of file (which usually  
        corresponds to the manufacturer, the recording system or to the  
        software used to create the file) and the particular subtype (e.g.  
        continuous, average).  
         
        Use as  
          type = ft_filetype(filename)  
          type = ft_filetype(dirname)  
         
        This gives you a descriptive string with the data type, and can be  
        used in a switch-statement. The descriptive string that is returned  
        usually is something like 'XXX_YYY'/ where XXX refers to the  
        manufacturer and YYY to the type of the data.  
         
        Alternatively, use as  
          flag = ft_filetype(filename, type)  
          flag = ft_filetype(dirname, type)  
        This gives you a boolean flag (0 or 1) indicating whether the file  
        is of the desired type, and can be used to check whether the  
        user-supplied file is what your subsequent code expects.  
         
        Alternatively, use as  
          flag = ft_filetype(dirlist, type)  
        where the dirlist contains a list of files contained within one  
        directory. This gives you a boolean vector indicating for each file  
        whether it is of the desired type.  
         
        Most filetypes of the following manufacturers and/or software programs are recognized  
         - 4D/BTi  
         - AFNI  
         - ASA  
         - Analyse  
         - Analyze/SPM  
         - BESA  
         - Bioimage Suite *.mgrid  
         - BrainSuite  
         - BrainVisa  
         - BrainVision  
         - Curry  
         - Dataq  
         - EDF  
         - EEProbe  
         - Elektra/Neuromag  
         - EEGsynth *.tsv  
         - FreeSurfer  
         - LORETA  
         - Localite  
         - MINC  
         - Neuralynx  
         - Neuroscan  
         - Nihon Koden *.m00  
         - OpenVibe MATLAB files *.mat  
         - Plexon  
         - SR Research Eyelink  
         - SensoMotoric Instruments (SMI) *.txt  
         - Tobii *.tsv  
         - Stanford *.ply  
         - Tucker Davis Technology  
         - CTF  
         - Yokogawa & Ricoh  
         - nifti, gifti  
         - Nicolet *.e (currently from Natus, formerly Carefusion, Viasys and Taugagreining. Also known as Oxford/Teca/Medelec Valor Nervus)  
         - Biopac *.acq  
         - AnyWave *.ades  
         - Qualisys *.tsv  
         - Mrtrix *.mif  
         - MAUS *.TextGrid  
         - Neurodata Without Borders *.nwb  
         - PhysioNet *.hea and *.dat  
         - NIRx *.tpl, *.wl1 and *.wl2  
         - York Instruments *.meghdf5  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_filetype.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_filetype", *args, **kwargs)

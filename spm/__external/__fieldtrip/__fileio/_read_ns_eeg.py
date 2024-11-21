from spm.__wrapper__ import Runtime


def _read_ns_eeg(*args, **kwargs):
    """
      READ_NS_EEG read a NeuroScan 3.x or 4.x EEG File  
         
        [eeg] = read_ns_eeg(filename, epoch)  
         
          filename     input Neuroscan .eeg file (version 3.x)  
          epoch        which epoch to read (default is all)  
          
        The output data structure eeg has the fields:  
          eeg.data(..)    - epoch signal in uV (size: Nepoch x Nchan x Npnt)  
        and  
          eeg.label       - electrode labels  
          eeg.nchan       - number of channels  
          eeg.npnt        - number of samplepoints in ERP waveform  
          eeg.time        - time for each sample  
          eeg.rate        - sample rate (Hz)  
          eeg.xmin        - prestimulus epoch start (e.g., -100 msec)  
          eeg.xmax        - poststimulus epoch end (e.g., 900 msec)  
          eeg.nsweeps     - number of accepted trials/sweeps  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ns_eeg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ns_eeg", *args, **kwargs)

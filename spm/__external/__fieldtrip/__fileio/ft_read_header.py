from spm.__wrapper__ import Runtime


def ft_read_header(*args, **kwargs):
    """
      FT_READ_HEADER reads header information from a variety of EEG, MEG and other time  
        series data files and represents the header information in a common  
        data-independent structure. The supported formats are listed below.  
         
        Use as  
          hdr = ft_read_header(filename, ...)  
         
        Additional options should be specified in key-value pairs and can be  
          'headerformat'   = string  
          'fallback'       = can be empty or 'biosig' (default = [])  
          'checkmaxfilter' = boolean, whether to check that maxfilter has been correctly applied (default = true)  
          'chanindx'       = list with channel indices in case of different sampling frequencies (only for EDF)  
          'chantype'       = string or cell-array with strings, channel types to be read (only for NeuroOmega and BlackRock)  
          'coordsys'       = string, 'head' or 'dewar' (default = 'head')  
          'headerformat'   = name of a MATLAB function that takes the filename as input (default is automatic)  
          'password'       = password structure for encrypted data set (for dhn_med10, mayo_mef30, mayo_mef21)  
          'readbids'       = string, 'yes', no', or 'ifmakessense', whether to read information from the BIDS sidecar files (default = 'ifmakessense')  
          'splitlabel'     = string, 'yes' or 'no', split the channel labels on the '-' and return the first part (default = 'yes' for CTF and FieldLine, 'no' for others)  
         
        This returns a header structure with the following fields  
          hdr.Fs          = sampling frequency  
          hdr.nChans      = number of channels  
          hdr.nSamples    = number of samples per trial  
          hdr.nSamplesPre = number of pre-trigger samples in each trial  
          hdr.nTrials     = number of trials  
          hdr.label       = Nx1 cell-array with the label of each channel  
          hdr.chantype    = Nx1 cell-array with the channel type, see FT_CHANTYPE  
          hdr.chanunit    = Nx1 cell-array with the physical units, see FT_CHANUNIT  
         
        For continuously recorded data, this will return nSamplesPre=0 and nTrials=1.  
         
        For some data formats that are recorded on animal electrophysiology  
        systems (e.g. Neuralynx, Plexon), the following optional fields are  
        returned, which allows for relating the timing of spike and LFP data  
          hdr.FirstTimeStamp      number, represented as 32-bit or 64-bit unsigned integer  
          hdr.TimeStampPerSample  number, represented in double precision  
         
        Depending on the file format, additional header information can be  
        returned in the hdr.orig subfield.  
         
        To use an external reading function, you can specify an external function as the  
        'headerformat' option. This function should take the filename as input argument.  
        Please check the code of this function for details, and search for BIDS_TSV as  
        example.  
         
        The following MEG dataformats are supported  
          CTF (*.ds, *.res4, *.meg4)  
          Neuromag/Elekta/Megin (*.fif)  
          BTi/4D (*.m4d, *.pdf, *.xyz)  
          Yokogawa/Ricoh (*.ave, *.con, *.raw)  
          NetMEG (*.nc)  
          ITAB - Chieti (*.mhd)  
          Tristan Babysquid (*.fif)  
          York Instruments (*.meghdf5)  
         
        The following EEG dataformats are supported  
          ANT - Advanced Neuro Technology, EEProbe (*.avr, *.eeg, *.cnt)  
          BCI2000 (*.dat)  
          Biosemi (*.bdf)  
          Bitalino OpenSignals (*.txt)  
          BrainVision (*.eeg, *.seg, *.dat, *.vhdr, *.vmrk)  
          CED - Cambridge Electronic Design (*.smr)  
          EGI - Electrical Geodesics, Inc. (*.egis, *.ave, *.gave, *.ses, *.raw, *.sbin, *.mff)  
          GTec (*.mat, *.hdf5)  
          GTec Unicorn (*.csv)  
          Generic data formats (*.edf, *.gdf)  
          Megis/BESA (*.avr, *.swf, *.besa)  
          Mega Neurone (directory)  
          Natus/Nicolet/Nervus (.e files)  
          Nihon Kohden (*.m00, *.EEG)  
          NeuroScan (*.eeg, *.cnt, *.avg)  
          Nexstim (*.nxe)  
          OpenBCI (*.txt)  
          TMSi (*.Poly5)  
         
        The following spike and LFP dataformats are supported  
          CED - Cambridge Electronic Design (*.smr)  
          MPI - Max Planck Institute (*.dap)  
          Neuralynx (*.ncs, *.nse, *.nts, *.nev, *.nrd, *.dma, *.log)  
          Neurodata Without Borders (*.nwb)  
          Neurosim  (neurosim_spikes, neurosim_signals, neurosim_ds)  
          NeuroOmega (*.mat transformed from *.mpx)  
          Neuropixel data recorded with SpikeGLX (*.bin, *.meta)  
          Plextor (*.nex, *.plx, *.ddt)  
          Windaq (*.wdq)  
         
        The following NIRS dataformats are supported  
          Artinis - Artinis Medical Systems B.V. (*.oxy3, *.oxy4, *.oxy5, *.oxyproj)  
          BUCN - Birkbeck college, London (*.txt)  
          SNIRF - Society for functional near-infrared spectroscopy (*.snirf)  
         
        The following Eyetracker dataformats are supported  
          EyeLink - SR Research (*.asc)  
          SensoMotoric Instruments - (*.txt)  
          Tobii - (*.tsv)  
         
        See also FT_READ_DATA, FT_READ_EVENT, FT_WRITE_DATA, FT_WRITE_EVENT,  
        FT_CHANTYPE, FT_CHANUNIT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_read_header.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_read_header", *args, **kwargs)

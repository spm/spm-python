from spm._runtime import Runtime


def _write_bdf(*args, **kwargs):
    r"""
      WRITE_BDF Write EEG data to a Biosemi BDF file  
         
          write_bdf(filename, data, fs, channel_names)  
          write_bdf(filename, data, fs, channel_names, 'Param', value, ...)  
         
        Inputs:  
          filename      - Output BDF filename (including .bdf extension)  
          data          - EEG data matrix (Nchannels × Ntimepoints)  
          fs            - Sampling frequency (Hz)  
          channel_names - Cell array of channel names (length Nchannels)  
         
        Optional parameters:  
          'SubjectID'   - Subject identification string (default: 'X')  
          'RecordingID' - Recording identification string (default: 'X')  
          'PhysicalMax' - Physical maximum for each channel (default: 32767)  
          'PhysicalMin' - Physical minimum for each channel (default: -32768)  
          'DigitalMax'  - Digital maximum for each channel (default: 8388607)  
          'DigitalMin'  - Digital minimum for each channel (default: -8388608)  
          'ScaleFactor' - Scaling factor for each channel (default: 1)  
          'Transducer'  - Transducer type for each channel (default: 'Active electrode')  
          'Prefilter'   - Prefiltering for each channel (default: 'HP:0.16Hz LP:500Hz')  
         
        Example:  
          data = randn(32, 1000); % 32 channels, 1000 timepoints  
          fs = 256; % 256 Hz sampling rate  
          ch_names = arrayfun(@(x) sprintf('EEG%02d', x), 1:32, 'UniformOutput', false);  
          write_bdf('test.bdf', data, fs, ch_names, 'SubjectID', 'SUBJ01');  
         
        See also READ_BDF  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/write_bdf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("write_bdf", *args, **kwargs, nargout=0)

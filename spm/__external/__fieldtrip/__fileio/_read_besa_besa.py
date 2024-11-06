from spm.__wrapper__ import Runtime


def _read_besa_besa(*args, **kwargs):
    """
      READ_BESA_BESA reads data and header information from a BESA file  
        See formatting document <a href="matlab:web(http://www.besa.de/downloads/file-formats/)">here</a>  
          
        Use as  
          [header] = read_besa_besa(filename);  
        where  
           filename        name of the datafile, including the .besa extension  
        This returns a header structure with the following elements  
          header.Fs           sampling frequency  
          header.nChans       number of channels  
          header.nSamples     number of samples per trial  
          header.nSamplesPre  number of pre-trigger samples in each trial  
          header.nTrials      number of trials  
          header.label        cell-array with labels of each channel  
          header.orig         detailed BESA header information  
         
        Use as  
          [header] = read_besa_besa(filename, [], chanindx);  
        where  
           filename        name of the datafile, including the .besa extension  
           chanindx        index of channels to read (optional, default is all)  
        This returns a header structure with the following elements  
          header.Fs           sampling frequency  
          header.nChans       number of channels  
          header.nSamples     number of samples per trial  
          header.nSamplesPre  number of pre-trigger samples in each trial  
          header.nTrials      number of trials  
          header.label        cell-array with labels of each channel  
          header.orig         detailed BESA header information  
         
        Or use as  
          [dat] = read_besa_besa(filename, header, begsample, endsample, chanindx);  
        where  
           filename        name of the datafile, including the .besa extension  
           header          header structure, see above  
           begsample       index of the first sample to read  
           endsample       index of the last sample to read  
           chanindx        index of channels to read (optional, default is all)  
        This returns a Nchans X Nsamples data matrix  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_besa_besa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_besa_besa", *args, **kwargs)

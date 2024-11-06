from spm.__wrapper__ import Runtime


def _read_biosemi_bdf(*args, **kwargs):
    """
      READ_BIOSEMI_BDF reads specified samples from a BDF continuous datafile  
        It neglects all trial boundaries as if the data was acquired in  
        non-continuous mode.  
         
        Use as  
          [hdr] = read_biosemi_bdf(filename);  
        where  
           filename        name of the datafile, including the .bdf extension  
        This returns a header structure with the following elements  
          hdr.Fs           sampling frequency  
          hdr.nChans       number of channels  
          hdr.nSamples     number of samples per trial  
          hdr.nSamplesPre  number of pre-trigger samples in each trial  
          hdr.nTrials      number of trials  
          hdr.label        cell-array with labels of each channel  
          hdr.orig         detailled EDF header information  
         
        Or use as  
          [dat] = read_biosemi_bdf(filename, hdr, begsample, endsample, chanindx);  
        where  
           filename        name of the datafile, including the .bdf extension  
           hdr             header structure, see above  
           begsample       index of the first sample to read  
           endsample       index of the last sample to read  
           chanindx        index of channels to read (optional, default is all)  
        This returns a Nchans X Nsamples data matrix  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_biosemi_bdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_biosemi_bdf", *args, **kwargs)

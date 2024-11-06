from spm.__wrapper__ import Runtime


def _read_edf(*args, **kwargs):
    """
      READ_EDF reads specified samples from an EDF datafile. It neglects all trial or  
        data block boundaries as if the data was acquired in non-continuous mode.  
         
        Note that since FieldTrip only accommodates a single sampling rate in a given  
        dataset, whereas EDF allows specification of a sampling rate for each channel.  If  
        there are heterogenous sampling rates then this function will automatically choose  
        a subset.  If the last such channel is different from the rest, the assumption will  
        be made that it is the annotation channel and the rest will be selected.  If that  
        is not the case, then the largest subset of channels with a consistent sampling  
        rate will be chosen.  To avoid this automatic selection process, the user may  
        specify their own choice of channels using chanindx.  In this case, the automatic  
        selection will only occur if the user selected channels still have heterogenous  
        sampling rates.  In this case the automatic selection will occur amongst the user  
        specified channels.  While reading the header the resulting channel selection  
        decision will be stored in hdr.orig.chansel and the contents of this field will  
        override chanindx during data reading.  
         
        Use as  
          [hdr] = read_edf(filename)  
        where  
           filename        name of the datafile, including the .edf extension  
        This returns a header structure with the following elements  
          hdr.Fs           sampling frequency  
          hdr.nChans       number of channels  
          hdr.nSamples     number of samples per trial  
          hdr.nSamplesPre  number of pre-trigger samples in each trial  
          hdr.nTrials      number of trials  
          hdr.label        cell-array with labels of each channel  
          hdr.orig         detailled EDF header information  
         
        Or use as  
          [dat] = read_edf(filename, hdr, begsample, endsample, chanindx)  
        where  
           filename        name of the datafile, including the .edf extension  
           hdr             header structure, see above  
           begsample       index of the first sample to read  
           endsample       index of the last sample to read  
           chanindx        index of channels to read (optional, default is all)  
        This returns a Nchans X Nsamples data matrix  
         
        Or use as  
          [evt] = read_edf(filename, hdr)  
        where  
           filename        name of the datafile, including the .edf extension  
           hdr             header structure, see above  
        This returns an Nsamples data vector of just the annotation channel  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_edf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_edf", *args, **kwargs)

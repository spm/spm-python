from spm.__wrapper__ import Runtime


def _read_nexstim_nxe(*args, **kwargs):
    """
      READ_NEXSTIM_NXE reads specified samples from a NXE continuous datafile  
         
        Use as  
          [hdr] = read_nexstim_nxe(filename)  
        where  
           filename        name of the datafile, including the .bdf extension  
        This returns a header structure with the following elements  
          hdr.Fs           sampling frequency  
          hdr.nChans       number of channels  
          hdr.nSamples     number of samples per trial  
          hdr.nSamplesPre  number of pre-trigger samples in each trial  
          hdr.nTrials      number of trials  
          hdr.label        cell-array with labels of each channel  
         
        Or use as  
          [dat] = read_nexstim_nxe(filename, begsample, endsample, chanindx)  
        where  
           filename        name of the datafile, including the .nxe extension  
           begsample       index of the first sample to read  
           endsample       index of the last sample to read  
           chanindx        index of channels to read (optional, default is all)  
        This returns a Nchans X Nsamples data matrix  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_nexstim_nxe.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_nexstim_nxe", *args, **kwargs)

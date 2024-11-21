from spm.__wrapper__ import Runtime


def _read_neuralynx_ds(*args, **kwargs):
    """
      READ_NEURALYNX_DS reads multiple single-channel Neuralynx files that are  
        all contained in a single directory. Each file is treated as a single  
        channel of a combined multi-channel dataset.  
         
        Use as  
          [hdr] = read_neuralynx_ds(dirname)  
          [dat] = read_neuralynx_ds(dirname, hdr, begsample, endsample, chanindx)  
         
        A Neuralynx dataset consists of a directory containing separate files,  
        one for each channel. All Neuralynx datafiles starts with a 16k header  
        (in ascii format), followed by an arbitrary number of data records. The  
        format of the data records depend on the type of data contained in the  
        channel (e.g. continuous or spike data).  
         
        To read the timestamps of spike waveforms (nse) or clustered spikes (nts),  
        the header should contain the fields  
          hdr.FirstTimeStamp  
          hdr.TimeStampPerSample  
        These can only be obtained from the corresponding simultaneous LFP  
        and/or MUA recordings.  
         
        See also READ_NEURALYNX_NCS, READ_NEURALYNX_NSE, READ_NEURALYNX_NTS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_ds.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuralynx_ds", *args, **kwargs)

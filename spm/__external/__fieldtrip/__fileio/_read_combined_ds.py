from spm.__wrapper__ import Runtime


def _read_combined_ds(*args, **kwargs):
    """
      READ_COMBINED_DS reads electrophysiological data from a collection  
        of files that are located in one directory, where each of the files  
        should contain one channel and should have the same sampling frequency  
        and number of samples as all other files.  
         
        Use as  
          hdr = read_combined_ds(dirname)  
          dat = read_combined_ds(dirname, hdr, begsample, endsample, chanindx)  
         
        This is supported for single channel files in one of the following formats  
          plexon_nex  
          neuralynx_bin  
          neuralynx_ncs  
          fcdc_matbin  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_combined_ds.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_combined_ds", *args, **kwargs)

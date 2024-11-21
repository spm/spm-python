from spm.__wrapper__ import Runtime


def _read_plexon_ddt(*args, **kwargs):
    """
      READ_PLEXON_DDT reads header or data from a Plexon *.ddt file,  
        which is a Plexon continuous data file optimized for continuous  
        (streaming) recording where every channel is continuously recorded  
        without gaps and the recording includes any dead time between spikes.  
          
        Use as  
          [hdr] = read_plexon_ddt(filename)  
          [dat] = read_plexon_ddt(filename, begsample, endsample)  
         
        samples start counting at 1  
        returned values are in mV  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_plexon_ddt.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_plexon_ddt", *args, **kwargs)

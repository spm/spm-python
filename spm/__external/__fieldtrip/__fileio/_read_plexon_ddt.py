from spm._runtime import Runtime


def _read_plexon_ddt(*args, **kwargs):
    r"""
      READ_PLEXON_DDT reads header or data from a Plexon *.ddt file,  
        which is a Plexon continuous data file optimized for continuous  
        (streaming) recording where every channel is continuously recorded  
        without gaps and the recording includes any dead time between spikes.  
          
        Use as  
          [hdr] = read_plexon_ddt(filename)  
          [dat] = read_plexon_ddt(filename, begsample, endsample)  
         
        samples start counting at 1  
        returned values are in mV  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_plexon_ddt.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_plexon_ddt", *args, **kwargs)

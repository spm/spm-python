from spm.__wrapper__ import Runtime


def ft_read_spike(*args, **kwargs):
    """
      FT_READ_SPIKE reads spike timestamps and waveforms from various data formats.  
         
        Use as  
         [spike] = ft_read_spike(filename, ...)  
         
        Additional options should be specified in key-value pairs and can be  
          'spikeformat' = string, described the fileformat (default is automatic)  
         
        The following file formats are supported  
          'blackrock_nev'  
          'mclust_t'  
          'neuralynx_ncs'  
          'neuralynx_nse'  
          'neuralynx_nst'  
          'neuralynx_ntt'  
          'neuralynx_nts'  
          'neuroshare'  
          'neurosim_spikes'  
          'nwb'  
          'plexon_ddt'  
          'plexon_nex'  
          'plexon_nex5'  
          'plexon_plx'  
          'wave_clus'  
         
        The output spike structure usually contains  
          spike.label     = 1xNchans cell-array, with channel labels  
          spike.waveform  = 1xNchans cell-array, each element contains a matrix (Nleads x Nsamples X Nspikes)  
          spike.waveformdimord = '{chan}_lead_time_spike'  
          spike.timestamp = 1xNchans cell-array, each element contains a vector (1 X Nspikes)  
          spike.unit      = 1xNchans cell-array, each element contains a vector (1 X Nspikes)  
        and is described in more detail in FT_DATATYPE_SPIKE  
         
        See also FT_DATATYPE_SPIKE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_read_spike.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_read_spike", *args, **kwargs)

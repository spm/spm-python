from spm._runtime import Runtime


def _read_ns_hdr(*args, **kwargs):
    r"""
      READ_NS_HDR read the header from a NeuroScan 3.x or 4.x AVG/EEG/CNT File  
         
        [hdr] = read_ns_hdr(filename)  
         
        The output data structure hdr has the fields:  
          hdr.label       - electrode labels  
          hdr.nchan       - number of channels  
          hdr.npnt        - number of samplepoints in ERP waveform  
          hdr.rate        - sample rate (Hz)  
          hdr.xmin        - prestimulus epoch start (e.g., -100 msec)  
          hdr.xmax        - poststimulus epoch end (e.g., 900 msec)  
          hdr.nsweeps     - number of accepted trials/sweeps  
          hdr.domain      - time (0) or frequency (1) domain  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_ns_hdr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ns_hdr", *args, **kwargs)

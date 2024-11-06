from spm.__wrapper__ import Runtime


def _read_ns_avg(*args, **kwargs):
    """
      READ_NS_AVG read a NeuroScan 3.x or 4.x AVG File  
         
        [avg] = read_ns_avg(filename)  
         
         The output data structure avg has the fields:  
          avg.data        - ERP signal in uV (Nchan x Npnt)  
          avg.nsweeps     - number of accepted trials/sweeps in avg  
          avg.variance    - variance of the signal (Nchan x Npnt)  
          avg.label       - electrode labels  
          avg.nchan       - number of channels  
          avg.npnt        - number of samplepoints in ERP waveform  
          avg.rate        - sample rate (Hz)  
          avg.time        - time for each sample OR  
          avg.frequency   - frequency for each sample  
          hdr.domain      - flag indicating time (0) or frequency (1) domain  
          avg.xmin        - prestimulus epoch start (e.g., -100 msec)  
          avg.xmax        - poststimulus epoch end (e.g., 900 msec)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ns_avg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ns_avg", *args, **kwargs)

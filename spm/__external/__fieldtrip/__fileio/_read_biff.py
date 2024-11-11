from spm.__wrapper__ import Runtime


def _read_biff(*args, **kwargs):
    """
      READ_BIFF reads data and header information from a BIFF file  
         
        This is a attemt for a reference implementation to read the BIFF  
        file format as defined by the Clinical Neurophysiology department of  
        the University Medical Centre, Nijmegen.  
         
        read all data and information  
          [data]  = read_biff(filename)  
        or read a selected top-level chunk  
          [chunk] = read_biff(filename, chunkID)  
         
        known top-level chunk id's are  
          data    : measured data         (matrix)  
          dati    : information on data       (struct)  
          expi    : information on experiment (struct)  
          pati    : information on patient    (struct)  
          evnt    : event markers         (struct)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_biff.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_biff", *args, **kwargs)

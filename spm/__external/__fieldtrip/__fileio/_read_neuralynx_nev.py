from spm.__wrapper__ import Runtime


def _read_neuralynx_nev(*args, **kwargs):
    """
      READ_NEURALYNX_NEV reads the event information from the *.nev file in a  
        Neuralynx dataset directory  
         
        Use as  
          nev = read_neuralynx_hdr(datadir, ...)  
          nev = read_neuralynx_hdr(eventfile, ...)  
         
        Optional input arguments should be specified in key-value pairs and may include  
          implementation  should be 1, 2 or 3 (default = 3)  
          value           number or list of numbers  
          mintimestamp    number  
          maxtimestamp    number  
          minnumber       number  
          maxnumber       number  
         
        The output structure contains all events and timestamps.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_nev.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuralynx_nev", *args, **kwargs)

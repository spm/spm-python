from spm.__wrapper__ import Runtime


def _read_neurosim_evolution(*args, **kwargs):
    """
      READ_NEUROSIM_EVOLUTION reads the "evolution" file that is written  
        by Jan van der Eerden's NeuroSim software. When a directory is used  
        as input, the default filename 'evolution' is read.  
         
        Use as  
          [hdr, dat] = read_neurosim_evolution(filename, ...)  
        where additional options should come in key-value pairs and can include  
          Vonly       = 0 or 1, only give the membrane potentials as output  
          headerOnly  = 0 or 1, only read the header information (skip the data), automatically set to 1 if nargout==1  
          
        See also FT_READ_HEADER, FT_READ_DATA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neurosim_evolution.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neurosim_evolution", *args, **kwargs)

from spm.__wrapper__ import Runtime


def _read_neurosim_spikes(*args, **kwargs):
    """
      READ_NEUROSIM_SPIKES reads the "spikes" file that is written by Jan  
        van der Eerden's NeuroSim software.  The output is represented in a  
        structure that is consistent with the FieldTrip spike representation.  
         
        OUTPUT  
        spike: A FieldTrip raw spike structure (including header information  
        in spike.hdr  
          
        INPUT  
        filename: name of spike files or directory (this will default to using  
        the 'spikes' file in the directory, the default neurosim naming  
        convention)  
          
        headerOnly: (OPTIONAL) if this is true, only the header information is  
        given directly as output, the spike data itself is not read in. (used by  
        FT_READ_HEADER)  
          
        See also FT_READ_SPIKE, FT_DATATYPE_SPIKE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neurosim_spikes.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neurosim_spikes", *args, **kwargs)

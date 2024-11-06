from spm.__wrapper__ import Runtime


def _read_neuromag_hc(*args, **kwargs):
    """
      READ_NEUROMAG_HC extracts the MEG headcoil marker positions from a neuromag  
        fif file or from the FieldTrip buffer  
         
        the definition of head coordinates is according to CTF standard:  
        - Origin: Intersection of the line through LPA and RPA and a line orthogonal  
          to L passing through the nasion  
        - X-axis from the origin towards the RPA point (exactly through)  
        - Y-axis from the origin towards the nasion (exactly through)  
        - Z-axis from the origin upwards orthogonal to the XY-plane  
         
        hc = read_neuromag_hc(filename)  
         
        returns a structure with the following fields  
          hc.dewar.nas    marker positions relative to dewar  
          hc.dewar.lpa  
          hc.dewar.rpa  
          hc.head.nas     marker positions relative to head (measured)  
          hc.head.lpa  
          hc.head.rpa  
          hc.standard.nas marker positions relative to head (expected)  
          hc.standard.lpa  
          hc.standard.rpa  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuromag_hc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuromag_hc", *args, **kwargs)

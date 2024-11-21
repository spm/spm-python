from spm.__wrapper__ import Runtime


def _snirf2opto(*args, **kwargs):
    """
      SNIRF2OPTO converts the SNIRF probe and measurementList structures to a FieldTrip  
        optode structure.  
         
        See https://github.com/fNIRS/snirf/blob/master/snirf_specification.md  
         
        The FieldTrip optode structure is defined in FT_DATATYPE_SENS  
         
        See also OPTO2HOMER, BTI2GRAD, CTF2GRAD, FIF2GRAD, ITAB2GRAD, MNE2GRAD, NETMEG2GRAD, YOKOGAWA2GRAD, FT_DATATYPE_SENS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/snirf2opto.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("snirf2opto", *args, **kwargs)

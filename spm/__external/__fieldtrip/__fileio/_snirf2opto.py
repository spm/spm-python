from spm._runtime import Runtime


def _snirf2opto(*args, **kwargs):
    r"""
      SNIRF2OPTO converts the SNIRF probe and measurementList structures to a FieldTrip  
        optode structure.  
         
        See https://github.com/fNIRS/snirf/blob/master/snirf_specification.md  
         
        The FieldTrip optode structure is defined in FT_DATATYPE_SENS  
         
        See also OPTO2HOMER, BTI2GRAD, CTF2GRAD, FIF2GRAD, ITAB2GRAD, MNE2GRAD, NETMEG2GRAD, YOKOGAWA2GRAD, FT_DATATYPE_SENS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/snirf2opto.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("snirf2opto", *args, **kwargs)

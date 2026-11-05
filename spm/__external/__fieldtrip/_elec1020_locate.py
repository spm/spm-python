from spm._runtime import Runtime


def _elec1020_locate(*args, **kwargs):
    r"""
      ELEC1020_LOCATE determines 10-20 (20%, 10% and 5%) electrode positions  
        on a scalp surface that is described by a triangulation  
         
        If you use this code, please cite:  
          Robert Oostenveld & Peter Praamstra (2001). The five percent electrode system  
          for high-resolution EEG and ERP measurements. Clin Neurophysiol.   
          doi: 10.1016/s1388-2457(00)00527-7.  
         
        See also EQUIDISTANT_LOCATE, FT_ELECTRODEPLACEMENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/elec1020_locate.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("elec1020_locate", *args, **kwargs)

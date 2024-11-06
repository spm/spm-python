from spm.__wrapper__ import Runtime


def spm_dcm_tfm_response(*args, **kwargs):
    """
      Display evoked and induced responses  
        FORMAT spm_dcm_tfm_response(xY,pst,hz,[XY])  
         
        xY.erp{i} - (t x n):         an array over t time bins and n channels for  
                                     condition i  
        xY.csd{i} - (t x w x n x n): an array over t time bins, w frequency bins  
                                     and n times n channels  
           pst - peristimulus time (seconds)  
           Hz  - frequency range   (Hz)  
         
        XY true value for overplotting  
       __________________________________________________________________________  
         
        This routine displays complex evoked and induced responses over peri-  
        stimulus time in terms of 90% confidence intervals about the ERP and as  
        images of the spectral density for each cannel:  
         
        see also spm_dcm_tfm_image - for between channel (coherence) responses)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_tfm_response.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_tfm_response", *args, **kwargs, nargout=0)

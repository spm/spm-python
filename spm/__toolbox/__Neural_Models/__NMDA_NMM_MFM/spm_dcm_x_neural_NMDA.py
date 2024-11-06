from spm.__wrapper__ import Runtime


def spm_dcm_x_neural_NMDA(*args, **kwargs):
    """
      Return the state and equation of neural mass models  
        FORMAT [x,f] = spm_dcm_x_neural_NMDA(P,'model')  
         
         P      - parameter structure  
        'model' - 'ERP','SEP','LFP','NNM' or 'MFM'  
         
        x   - initial states  
        f   - state euquation  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/NMDA_NMM_MFM/spm_dcm_x_neural_NMDA.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_x_neural_NMDA", *args, **kwargs)

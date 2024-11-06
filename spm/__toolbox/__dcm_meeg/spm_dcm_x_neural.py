from spm.__wrapper__ import Runtime


def spm_dcm_x_neural(*args, **kwargs):
    """
      Return the state and equation of neural mass models  
        FORMAT [x,f,h] = spm_dcm_x_neural(P,'model')  
         
         P      - parameter structure  
        'model' - 'ERP','SEP','CMC','LFP','CMM','NNM', 'MFM' or 'CMM NMDA'  
         
        x   - initial states  
        f   - state equation dxdt = f(x,u,P,M)  - synaptic activity  
        h   - state equation dPdt = f(x,u,P,M)  - synaptic plasticity  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_x_neural.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_x_neural", *args, **kwargs)

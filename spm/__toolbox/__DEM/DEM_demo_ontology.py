from spm.__wrapper__ import Runtime


def DEM_demo_ontology(*args, **kwargs):
    """
      This demonstration routine illustrates how a generative model can be used  
        to furnish a computational nosology. In brief, it generates symptoms and  
        diagnostic profiles from hidden or latent exogenous causes (e.g.,  
        therapeutic interventions) that are mediated by latent (pathophysiological  
        and psychopathological) states.  Pathophysiological trajectories  are  
        modelled with a Lorenz attractor that (with a linear mapping)  
        produces (two-dimensional) psychopathology. In turn, the  
        psychopathological states generate symptoms (with a non-linear function  
        of linear mixtures) and diagnostic outcomes (with a softmax function of  
        diagnostic potential). The psychopathological state of a subject is  
        associated with a diagnostic potential in terms of its Euclidean distance  
        from disease categories (locations in the associated state space).  
         
        We start by simulating a relapsing-remitting disease process and then  
        infer the latent states and parameters of a particular subject.  
        This is then repeated in the setting of a therapeutic intervention.  
        The demonstration then briefly considers model identification and  
        selection by focusing on the mapping between pathophysiology and  
        psychopathology. Finally, We consider, prognosis and prediction by  
        estimating subject-specific parameters prior to therapy and then  
        predicting putative response in the future, based upon a posterior  
        predictive density.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_ontology.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_ontology", *args, **kwargs, nargout=0)

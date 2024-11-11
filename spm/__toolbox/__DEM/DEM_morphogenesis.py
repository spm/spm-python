from spm.__wrapper__ import Runtime


def DEM_morphogenesis(*args, **kwargs):
    """
      This routine illustrates self-assembly or more for genesis under active  
        inference (free energy minimisation).  It exploits the fact that one can  
        express a systems (marginal) Lyapunov function in terms of a variational  
        free energy.  This means that one can prescribe an attracting set in  
        terms of the generative model that defines variational free energy.  In  
        this example, the attracting set is a point attractor in the phase space  
        of a multi-celled organism: where the states correspond to the location  
        and (chemotactic) signal expression of 16 cells.  The generative model  
        and process are remarkably simple; however, the ensuing migration and  
        differentiation of the 16 cells illustrates self-assembly - in the sense  
        that each cell starts of in the same location and releasing the same  
        signals.  In essence, the systems dynamics rest upon each cell inferring  
        its unique identity (in relation to all others) and behaving in accord  
        with those inferences; in other words, inferring its place in the  
        assembly and behaving accordingly.  Note that in this example there are  
        no hidden states and everything is expressed in terms of hidden causes  
        (because the attracting set is a point attractor)  Graphics are produced  
        illustrating the morphogenesis using colour codes to indicate the cell  
        type - that is interpreted in terms of genetic and epigenetic  
        processing.  
        _________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_morphogenesis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_morphogenesis", *args, **kwargs)

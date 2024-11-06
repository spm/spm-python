from spm.__wrapper__ import Runtime


def spm_dcm_J(*args, **kwargs):
    """
      VOI extraction of adjusted data and Markov Blanket decomposition  
        FORMAT [J,K] = spm_dcm_J(Y,U,X0,dt,R,I,D)  
         
        Y  - response variable  
        U  - exogenous inputs  
        XO - confounds  
        dt - time bin  
        R  - distance matrix  
        I  - self inhibition [default: -1]  
        D  - upper bound on distance (mm) [default: 64]  
         
        J(nv,nv)  - Jacobian  
        K(nv,nu)  - input block  
         
       __________________________________________________________________________  
        This routine evaluates the effective connectivity of a dynamic causal  
        model based upon the Jacobian (i.e., state matrix) of a stochastic  
        differential equation. In other words, it approximates the coupling among  
        hidden states to first order, under some simplifying assumptions.  
        Starting from a linear state space model, in which the response variable  
        (y) is a linear convolution (K) of some hidden states (x) subject to  
        observation and system noise (r and e) respectively, we have:  
         
        D*x = x*J' + e  => K*D*x = K*x*J' + K*e = D*y = y*J' + K*e + D*r - r*J'  
        y   = K*x  + r  =>   D*y = K*D*x  + D*r  
         
        This means we can approximate the system with a general linear model:  
         
        D*y = y*J' + w:   cov(w) = h(1)*K*K' + h(2)*D*D' + h(3)*I  
         
        Where, h(3)*I  = h(2)*J*J', approximately; noting that the leading  
        diagonal of J will dominate (and be negative). If K is specified in terms  
        of convolution kernels, then the covariance components of the linearised  
        system can be expressed as:  
         
        K = k(1)*K{1} + k(2)*K{2} + ...  
          => K*K' = k(1)*k(1)*K{1}*K{1}' + k(1)*k(2)*K{1}*K{2}' ...  
         
        Where k(i)*k(j) replaces the [hyper]parameter h(1) above. This linearized  
        system can be solved using parametric empirical Bayes (PEB) for each  
        response variable, under the simplifying assumption that there are the  
        same number of observations and hidden states.  
         
        This allows large graphs to be inverted by considering the afferents  
        (i.e., influences on) to each node sequentially. Redundant elements of  
        the Jacobian (i.e., connections) are subsequently removed using Bayesian  
        model reduction (BMR). The result is a sparse Jacobian that corresponds  
        to the coupling among hidden states that generate observed double  
        responses, to first-order.  
         
        See: Frassle S, Lomakina EI, Kasper L, Manjaly ZM, Leff A, Pruessmann KP,  
        Buhmann JM, Stephan KE. A generative model of whole-brain effective  
        connectivity.Neuroimage. 2018 Oct 1;179:505-529.  
         
        GRAPHICAL OUTPUT Sparse connectivity: the figure illustrates the sparsity  
        of effective connectivity using Bayesian model reduction. The left panel  
        shows the log evidence for a series of models that preclude connections  
        beyond a certain distance or radius. This log evidence is been normalised  
        to the log evidence of the model with the least marginal likelihood. The  
        middle panel shows the ensuing sparse coupling (within the upper bound of  
        D mm) as an adjacency matrix, where particles have been ordered using a  
        nearest neighbour scheme in voxel space. The blue dots indicate  
        connections that have been removed by Bayesian model reduction. The right  
        panel zooms in on the first 32 particles, to show local connections that  
        were retained (red) or removed (blue).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_J.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_J", *args, **kwargs)

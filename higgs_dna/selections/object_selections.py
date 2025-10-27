import awkward
import numpy as np

def deltaR(eta1, phi1, eta2, phi2):

    invalid_mask = (eta1 == -999) | (phi1 == -999) | (eta2 == -999) | (phi2 == -999) | (eta1 is None) | (phi1 is None) | (eta2 is None) | (phi2 is None)

    # calculate delta_r, making sure to handle the periodicity of phi
    dphi = (phi1 - phi2 + np.pi) % (2 * np.pi) - np.pi
    deta = eta1 - eta2

    dr = np.sqrt(deta**2 + dphi**2)

    # set invalid values to -999
    dr = awkward.where(invalid_mask, -999, dr)
    dr = awkward.fill_none(dr, -999)

    return dr

def delta_r_mask(
    first: awkward.highlevel.Array, second: awkward.highlevel.Array, threshold: float
) -> awkward.highlevel.Array:
    """
    Select objects from first which are at least threshold away from all objects in second.
    The result is a mask (i.e., a boolean array) of the same shape as first.

    :param first: objects which are required to be at least threshold away from all objects in second
    :type first: coffea.nanoevents.methods.candidate.PtEtaPhiMCandidate
    :param second: objects which are all objects in first must be at leats threshold away from
    :type second: coffea.nanoevents.methods.candidate.PtEtaPhiMCandidate
    :param threshold: minimum delta R between objects
    :type threshold: float
    :return: boolean array of objects in objects1 which pass delta_R requirement
    :rtype: coffea.nanoevents.methods.candidate.PtEtaPhiMCandidate
    """
    mval = first.metric_table(second)
    return awkward.all(mval > threshold, axis=-1)


def delta_phi_mask(
        Phi1: awkward.highlevel.Array,
        Phi2: awkward.highlevel.Array,
        threshold: float
) -> awkward.highlevel.Array:
    # Select objects that are at least threshold away in Phi space

    # calculate delta_phi
    dPhi = abs(Phi1 - Phi2) % (2 * np.pi)
    dPhi = awkward.where(dPhi > np.pi, 2 * np.pi - dPhi, dPhi)

    return dPhi > threshold
